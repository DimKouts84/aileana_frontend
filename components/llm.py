from dotenv import load_dotenv
from . import databases as db 
from . import visualizations as viz
# import databases as db
# import visualizations as viz
import pandas as pd
import plotly.express as px
import os, requests, time

load_dotenv()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ LLM Models ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# OpenRouter
or_llama33_70B_inst, llama_31_70_inst_free, qwen_25_72b = 'meta-llama/llama-3.3-70b-instruct', 'meta-llama/llama-3.1-70b-instruct:free', 'qwen/qwen-2.5-72b-instruct'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ LLM Provider Connections ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OPENROUTER_COMPLETIONS_URL = os.getenv("OPENROUTER_COMPLETIONS_URL")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ LLM Provider Configuration ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
provider_url_to_be_used = OPENROUTER_COMPLETIONS_URL
provider_key_to_be_used = OPENROUTER_API_KEY
provider_model_to_be_used = qwen_25_72b

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Prompts ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
graph_db_schema = '''
    **Nodes**
    ["INDUSTRY"] : ["industry_name", "standardized_industry_name"]
    ["JOB"] : ["employment_type", "employment_model", "job_seniority", "minimum_level_of_education", "standardized_occupation", "job_title", "country", "job_reference", "job_description"]
    ["SKILL"] : ["skill_name", "skill_category", "skill_type"]
    ["EXPERIENCE"] : ["minimum_years", "years_required"]
    ["BENEFIT"] : ["benefit_name"]
    ["RESPONSIBILITY"] " ["description"]
    ["ACADEMIC_DEGREE"] : ["degree_name", "degree_type", "degree_category"]
    ["CERTIFICATION"] : ["certification_name", "certification_type", "certification_category"]
    
    **Relationships**
    (JOB)-[:REQUIRES]->(ACADEMIC_DEGREE)
    (JOB)-[:HAS]->(RESPONSIBILITY)
    (JOB)-[:OFFERS]->(BENEFIT)
    (JOB)-[:REQUIRES]->(EXPERIENCE)
    (JOB)-[:NEEDS]->(SKILL)
    (JOB)-[:REQUIRES]->(CERTIFICATION)
    (JOB)<-[:POSTS]-(INDUSTRY)
    (INDUSTRY)<-[:BELONGS_TO]-(INDUSTRY_NAME)
    '''

cypher_query_examples = '''
    - **Example 1:** 
    -- Question: 'I want to know the skills required for an "accountant".'
    -- Cypher: 
        'MATCH (j:JOB)-[r]-(s:SKILL)
        WHERE toLower(j.job_title) CONTAINS toLower("Accountant") OR toLower(j.standardized_occupation) CONTAINS toLower("Accountant")
        RETURN s.skill_name AS skill_name, count(*) AS skill_count
        ORDER BY skill_count DESC
        LIMIT 100'
    
    - **Example 2:**
    -- Question: 'I want to know the industries related to "food" what kind of jobs they offer / post.'
    -- Cypher:
        'MATCH (i:INDUSTRY)-[r]->(j:JOB)
        WHERE toLower(i.industry_name) CONTAINS toLower("food")
        WITH j.job_title AS job_title, count(*) AS job_count
        RETURN job_title, job_count
        ORDER BY job_count DESC
        LIMIT 100'
    
    - **Example 3:**
    -- Question: I have great knowledge of Excel and have a degree on Biology, what kind of jobs can I find?
    -- Cypher:
        '
        '
        
    - **Example 4:**
    -- Question: 'I'm a front-end developer and I know Django and Angular, what other skills are required for jobs?'
    -- Cypher:
        'MATCH (j:JOB)-[r]-(s:SKILL)
        WHERE toLower(j.job_title) CONTAINS toLower("Front-end") OR toLower(j.job_title) CONTAINS toLower("Frontend")
        RETURN s.skill_name AS skill_name, count(*) AS skill_count, j.job_title
        ORDER BY skill_count DESC
        LIMIT 100'
        
    - **Example 5:**
    -- Question: 'I want to work from home, what kind of jobs offer this flexibility?'
    -- Cypher:
        'MATCH (j:JOB)
        WHERE toLower(j.employment_model) CONTAINS toLower("remote") OR toLower(j.employment_model) CONTAINS toLower("hybrid") OR toLower(j.employment_type) CONTAINS toLower("remote") OR toLower(j.employment_type) CONTAINS toLower("home")
        RETURN j.job_title AS job_title, j.standardized_occupation AS standardized_occupation, count(*) AS job_count, j.employment_model AS employment_model
        ORDER BY job_count DESC
        LIMIT 100'
    
    - **Example 6:**
    -- Question: 'I want to know which industries require a degree in Biology.'
    -- Cypher:
        'MATCH (d:ACADEMIC_DEGREE)
        WHERE toLower(d.degree_field) CONTAINS toLower("accounting")
        MATCH (d)-[r1]-(j:JOB)-[r2]-(i:INDUSTRY)
        RETURN i.standardized_industry_name AS industry, 
            COUNT(*) AS job_count
        ORDER BY job_count DESC
        LIMIT 100'

    - **Example 7:**
    -- Question: 'I want to know which jobs require a degree in Biology.'
    -- Cypher:
        'MATCH (d:ACADEMIC_DEGREE)
        WHERE toLower(d.degree_field) CONTAINS toLower("biology")
        MATCH (d)<-[r1]-(j:JOB)
        RETURN j.job_title AS job_title, 
            COUNT(*) AS job_count
        ORDER BY job_count DESC
        LIMIT 100'
    '''


data_engineer_system_prompt = f'''
    You are an expert Knowledge graph database analyst.
    Your role is to help provide Cypher queries to the chatbot to retrieve information from the Neo4J Database, following the instructions below:
    1. Generate Cypher query compatible ONLY for Neo4j Version 5.
    2. Do not use EXISTS, SIZE, HAVING keywords in the cypher. Use alias when using the WITH keyword.
    3. Use only Nodes, Node labels, and Relationships that are mentioned in the given schema.
    4. Always do a case-insensitive and fuzzy search for any properties related search.
    6. You try to use similar keywords to the user's question to retrieve the information (e.g. `software developer`, `software engineer` and `software programmer`).
    7. Never use relationships that are not mentioned in the given Graph Database Schema: {graph_db_schema}.
    8. Here are some examples: {cypher_query_examples}
    9. If the question does not need a Cypher query, please output `NONE` as a string.
    
    '''


occupational_analyst_system_prompt = f'''
    You are very excited and happy occupational expert analyst eager to answer questions about the job market in Cyprus.
    Your role is to take data provided by a data engineer (if requested by the user) and answer to the user's questions.
    Provide your using tables or bullet points to make your point more clear, if necessary.
    Your output is always VERY professional and informative.
    '''

visualizations_system_prompt = f'''
    You are a data visualization expert.
    Your role is to provide visualizations of the data provided by the data engineer and the occupational analyst.
    Your output is always be a Plotly "figure" that can be used for creating visualizations.
    Example:
    - Examples of what will your output look like:
        'your_output' ---> "px.treemap(df, path=["industry"], values="job_postings", title="Top 10 Industries by Number of Job Postings")"
        'your_output' ---> "px.bar(df, x='industry', y='job_postings', title='Top 10 Industries by Number of Job Postings')"
        or
        'your_output' ---> "px.pie(df, names='industry', values='job_postings', title='Top 10 Industries by Number of Job Postings')"
    - How it ill be used: 
        "def generate_visualization(your_output):
            fig = your_output
            st.plotly_chart(fig)
            return"
    You will ONLY provide the Plotly that will be used for the visualizations. Nothing ELSE.
    '''


# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Call LLM Function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def call_LLM_API_JSON(provider_model_to_be_used, system_prompt, user_prompt_for_parsing, temperature=0, max_retries=3):
    # Note for Models that worked well, especially with the JSON mode:
    ## Models with the best quality of output:  lmstudio-community/Qwen2.5-14B-Instruct-Q4_K_M.gguf,  lmstudio-community/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
    ## Models that worked ok: MaziyarPanahi/Qwen2.5-7B-Instruct-Uncensored.Q5_K_S.gguf, bartowski/Llama-3.2-3B-Instruct-f16.gguf
    
    # Prepare the headers 
    url = provider_url_to_be_used
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {provider_key_to_be_used}',
    }

    # Prepare the messages for the chat completion
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for_parsing}
    ]
    # Prepare the payload
    payload = {
        'model': provider_model_to_be_used,
        'messages': messages,
        "type": "json_object",
        'temperature': temperature,
        'max_tokens': 9216
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            if not response.ok:
                print(f"API Error: {response.status_code}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                    continue
                return None
            
            response_json = response.json()
            
            # Check if response has expected structure
            if 'choices' not in response_json:
                print("Unexpected API response format")
                print(response_json)  # Display actual response for debugging
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return None
            
            content = response_json['choices'][0]['message']['content']
            if content:
                return content
            else:
                print("Empty content received from API")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return None

        except requests.RequestException as e:
            print(f"Request error on attempt {attempt + 1}/{max_retries}: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            return f"Error: {str(e)} response from LLM API."
        except Exception as e:
            print(f"Unexpected error on attempt {attempt + 1}/{max_retries}: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            return None
    
    return None

    
    
# A function that takes a question from the user to create a Cypher query
def query_to_data_engineer(data_engineer_system_prompt, question, temperature):
    
    user_promt = f'''
    Based on the user's question provide a Cypher query to retrieve the information from the Neo4J Database. 
    The question:{question}.
    
    Output if it is required by the question. The Cypher MUST as a string (e.g.: MATCH (j:JOB)-[r]-(s:SKILL)) NOT as Markdown (e.g.: using ```cypher ... ```) 
    Output `NONE` if the question does not need a Cypher query.
    '''
    
    response = call_LLM_API_JSON(provider_model_to_be_used, data_engineer_system_prompt, user_promt,temperature)
    return response


def query_to_occupational_analyst(occupational_analyst_system_prompt, question, graph_data, temperature):

    user_promt = f'''
    You will receive a question from a user
    Question {question} \n
    The data: {graph_data} \n
    '''
    
    response = call_LLM_API_JSON(provider_model_to_be_used, occupational_analyst_system_prompt, user_promt, temperature)
    return response

def query_to_visualizations(visualizations_system_prompt, question, graph_data, temperature):
    
    user_promt = f'''
    You will receive the following data: {graph_data} \n
    Based on the data, return ONLY the Plotly "figure" that can be used for creating visualizations as per the examples.
    '''
    
    response = call_LLM_API_JSON(provider_model_to_be_used, visualizations_system_prompt, user_promt, temperature)
    print(f"---- Visualization Response:\n{response}\n")
        # Execute the returned plotting code to create actual figure
    try:
        # Convert DataFrame if needed
        df = pd.DataFrame(graph_data)
        # Safely evaluate the Plotly code
        fig = eval(response)
        print(f"---- Visualization Figure:\n{fig}\n")
        return fig
    except Exception as e:
        print(f"Error creating visualization: {e}")
        return None
    return response

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Test the LLM Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# question = "Can you provide me with career advise? What should I have or do to be a Data Analyst?"
# cipher_query = query_to_data_engineer(data_engineer_system_prompt, question, 0)
# print(f"---- Cipher Query:\n{cipher_query}\n")

# if cipher_query == "NONE":
#     print("---- No Cypher query needed for the question.\n")
#     graph_data = "No job related information available"
# else:
#     graph_data = db.get_job_data_from_Cypher(cipher_query)
#     # print(f"---- Graph Data:\n{graph_data}\n")
#     fig = query_to_visualizations(visualizations_system_prompt, question, graph_data, 0)
#     if fig is not None:
#         viz.generate_visualization(graph_data, fig)

# time.sleep(5)  # Optional: wait a bit before retrying

# occupational_analyst_answer = query_to_occupational_analyst(occupational_analyst_system_prompt, question, graph_data, 1)
# print(f"---- Occupational Analyst's Answer:\n{occupational_analyst_answer}\n")
