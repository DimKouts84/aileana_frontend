import streamlit as st
from dotenv import load_dotenv
import os
import shelve

load_dotenv()

# Load chat history from shelve file
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])


# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages


# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])



# A function that takes a question from the user to create a Cypher query
def query_to_data_analyst(question):
    graph_db_schma = """
    **Nodes**
    [(:BENEFIT {name: "BENEFIT", indexes: [], constraints: []}), (:INDUSTRY {name: "INDUSTRY", indexes: [], constraints: []}), (:SKILL {name: "SKILL", indexes: [], constraints: []}), (:EXPERIENCE {name: "EXPERIENCE", indexes: [], constraints: []}), (:JOB {name: "JOB", indexes: ["embedding"], constraints: []}), (:RESPONSIBILITY {name: "RESPONSIBILITY", indexes: [], constraints: []})]
    
    **Relationships**
    [[:NEEDS {name: "NEEDS"}], [:REQUIRES {name: "REQUIRES"}], [:HAS {name: "HAS"}], [:OFFERS {name: "OFFERS"}], [:POSTS {name: "POSTS"}]]
    
    **Node labels**
    ["INDUSTRY"] : ["industry_name", "standardized_industry_name"]
    ["JOB"] : ["employment_type", "employment_model", "job_seniority", "minimum_level_of_education", "standardized_occupation", "job_title", "country", "job_reference", "job_description"]
    ["SKILL"] : ["skill_name", "skill_category", "skill_type"]
    ["EXPERIENCE"] : ["minimum_years", "years_required"]
    ["BENEFIT"] : ["benefit_name"]
    ["RESPONSIBILITY"] " ["description"]
    """
    
    system_prompt = f'''
    YYou are an expert Knowledge graph database analyst.
    Your role is to help provide Cypher queries to the chatbot to retrieve information from the Neo4J Database.
    Based on the schema of the graph database, here are the nodes, the node labels and relationships that you can query: {graph_db_schma}.
    You will ONLY output a Cypher query, NO OTHER INFORMATION.'''
    promt = f'''Based on the user's question provide a Cypher query to retrieve the information from the Neo4J Database. {question}?'''

    
    # answer = f"Here are some nodes related to your question: {data}"
    return



def query_to_occupational_analyst(question, data_from_chatbot):
    
    system_prompt = f'''
    You are very excited Occupational expert analyst eager to answer questions about the job market.
    Your role is to take data provided by a data engineer and answer to the User's questions.'''
    promt = f'''You will receive a question from a user
    {question}?'''
    with driver.session() as session:
        query = f""" Answer to the user's question based on the data provided by the data engineer.
        The data: {data_from_chatbot} \n
        The user's question: {question}
        Now be helpful and provide your answer.
        """
        result = session.run(query)
        data = [record.data() for record in result]
    # Format the data into a response
    answer = f'''Here are some nodes related to your question: {data}'''
    return answer

