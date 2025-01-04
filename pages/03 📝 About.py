import streamlit as st
from components.sidebar_auth import init_sidebar_auth
from components import widgets

# Page Configuration
st.set_page_config(
    page_title="About",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Initialize auth in sidebar
user_email = init_sidebar_auth()


widgets.hero_section(
        title= "About Aileana",
        subtitle="🛠️ Technical and other information on the project and the 📝 'Terms and Conditions'.",
    )

st.markdown('''
# Aileana

> **Let the job market tell you a story!**

**Aileana**  is an agentic GenAI pipeline for automated data extraction, classification, and analysis. It is also accompanied by an LLM chatbot with a deep understanding of the job market, which assists individuals in navigating their career paths and HQ professionals write better job postings.

As a system of GenAI agents, “she” can expertly analyse job postings create correlations and find similarities between jobs, skills, academic knowledge, requirements, benefits, required experience, and responsibilities. Aileana achieves this by utilizing state-of-the-art LLM models and Retrieval-Augmented Generation (RAG), enhancing accuracy and reliability with data fetched from recent and real sources. The Knowledge Graph database helps the models make more detailed queries and delve deeper than traditional vector embeddings in SQL databases.

---

## 💬 The Story

**Eleana** was nearly 18 years old, facing the critical decision of choosing her career and relevant academic studies.

She had a passion for Biology *(or at least thought she did)* , but no one in her family or circle was familiar with this field, and the job prospects were uncertain 🤔.

Given my background in the health domain, she asked me if pursuing Biology was a good idea. My response was something like: " *If it is your passion, follow it.* "

However, this answer was *generic* and  *insincere* , to be honest. The truth was that *I had no idea.* This led me to ponder:

* Is it really good advice? Is 'liking' a subject the only criterion for choosing a field of study?
* What are the employment prospects after graduation?
* What related jobs are available, and what other skills are needed to qualify for these jobs?
* What benefits do such jobs usually offer?

As a data nerd 🤓, I realized the job market operates like any other market:

* Supply and demand are key driving forces.
* Higher qualifications/specializations generally lead to higher pay.

Only *data* can provide answers to these questions, not anecdotal experiences.

Thus,  ***Aileana*** , this project, was born.
''')

# Some space between Paragraphs
st.write(" ")
st.write(" ")
st.write("---") # Division Line

st.write('''
## ⚡️Tech Stack

| Category                  | Technology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend**           | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                              |
| **Backend**            | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Databases**          | ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white) ![Neo4j](https://img.shields.io/badge/-Neo4j-008CC1?style=flat&logo=neo4j&logoColor=white)                                                                                                                                                                                                                                                                                                  |
| **Web Scraping**       | ![Beautiful Soup](https://img.shields.io/badge/-Beautiful_Soup-FFD700?style=flat&logo=beautiful-soup&logoColor=black) ![Selenium](https://img.shields.io/badge/-Selenium-43B02A?style=flat&logo=selenium&logoColor=white)                                                                                                                                                                                                                                                                             |
| **Data Processing**    | ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Data Visualization** | ![Plotly](https://img.shields.io/badge/-Plotly-239120?style=flat&logo=plotly&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                       |
| **DevOps**             | ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                       |
| **GenAI Tect Stack**   | ![Langchain](https://img.shields.io/badge/-Langchain-FF4B4B?style=flat&logo=langchain&logoColor=white) ![Groq](https://img.shields.io/badge/-Groq-FFA200?style=flat&logo=groq&logoColor=Orange) ![Llama 3.2](https://img.shields.io/badge/-Ollama-FF4B4B?style=flat&logo=ollama&logoColor=white) ![Qwen 2.5](https://img.shields.io/badge/-Qwen-FF4B4B?style=flat&logo=qwen&logoColor=white) ![Hugging Face](https://img.shields.io/badge/-Hugging_Face-FFD700?style=flat&logo=huggingface&logoColor=white) ![OpenRouter](https://img.shields.io/badge/-OpenRouter-43B02A?style=flat&logo=openrouter&logoColor=white) |


> Feel free to can use the `requirements.txt` to `pip install` all dependancies in the project environment.         
''')

# Some space between Paragraphs
st.write(" ")
st.write(" ")
st.write("---") # Division Line

# Load images first
with open('static\graph_shcema.png', 'rb') as f:
    graph_schema = f.read()


# Combined text and images in one st.write
st.write('''
##  The Graph-RAG
##### Retrieval Augmented Generation with Knowledge Graph Database

The entire app, visualization and chat interface is powered by a Knowledge Graph Database. This architecture combines the power of graph databases with modern LLM technology to create a more intelligent and context-aware system.

Unlike traditional relational databases, graph databases excel at handling complex relationships and interconnected data. In our case, this means:
* 🔗 Better representation of job market relationships
* ⚡ Faster querying of connected data
* 🧩 More intuitive modeling of real-world relationships
* 🔍 Enhanced ability to discover hidden patterns

##### How RAG Enhances Aileana 🚀
The Retrieval Augmented Generation (RAG) approach:
1. 💾 Stores processed job market data in our graph database
2. 🎯 Retrieves relevant information based on user queries
3. 🧠 Augments LLM responses with factual, up-to-date data
4. ✨ Provides more accurate and contextual answers
''')

st.write(" ")

st.write('''
         >Below is our graph schema showing how different entities relate to each other.
         ''')         
st.image(graph_schema, caption='Graph Database Schema and Relationships')


# Some space between Paragraphs
st.write(" ")
st.write(" ")
st.write("---") # Division Line

st.write('''

## 🚀 Conclusions

### ⚡️The Tech

Using high quality LLMs locally was really difficult and not cost effective. This is why I used hosted LLMs like LLama 3.2 and QWEN 2.4 on cloude services like GROQ and OpenRouter. 

This powerhouse combination makes extracting key information from job listings a breeze! It was so fast and easy that I even used LLMs for simple tasks like text translations. After cross-checking the response from OpenAI's Chat-GPT4o, the results were surprisingly close, making it a no-brainer due to the cost ( and speed! ) difference.

While one database could suffice, I initially planned to use the PGVector add-on for PostgreSQL. However, after parsing a few thousand listings 😅, I realized leveraging LLMs (Large Language Models) for data extraction was a brilliant move for a data analysis project. This approach becomes even more exciting when combined with a Knowledge Graph database like Neo4J - it's a dream come true for my inner data geek 🔍!
''')



# Some space between Paragraphs
st.write(" ")
st.write(" ")
st.write("---") # Division Line

st.write('''
### 💭A Few Thoughts

This project is my cool experiment to see if we can really put Large Language Models (LLMs) and agentic frameworks like [LangChain](https://langchain.com/) and [CrewAI](https://www.crewai.com/) into production. Spoiler alert: it's a wild ride, flaws and all!

Sure, these tools are reliable...ish. They're consistent...ish. But are they perfect? Not quite. Sometimes, even with simple text, different models can give you wildly different results 🔍.

Designing an LLM-based solution isn't just plug-and-play. You've got to juggle tokens, output formats (think JSON), and the cost and reliability of parameters like `temperature`. And don't even get me started on prompt engineering – it's an art form, not a science 😎!

Oh, and did I mention tools? LLMs can now use them, but in reality, creating custom tools can sometimes lead to a bigger codebase. Sometimes, a simple script does the trick better.

Now, let's talk unit testing. Setting up self-checking for LLMs can seriously boost response accuracy. But here's the catch: writing these self-checking methods is a whole other ball game because every agent and every API use case is different.... be prepared for a cost hike and a flurry of API calls 💸.

On the other hand, when you need to go through hundreds or thousands of paragraphs to extract valuable information, you need brains... and lots of them 🧠🧠🧠.

LLMs are the only solution for such tasks at scale!
''')

# Some space between Paragraphs
st.write(" ")
st.write(" ")
st.write("---") # Division Line

st.write('''
### The Takeaway 🎉

So, what's the takeaway? The fewer decisions a model has to make, the more reliable it will be. But that also means more API calls and, yep, higher costs.

if you went that far, I hope you enjoyed this tech adventure🎉!
         ''')


# Some space between Paragraphs
st.write(" ")
st.write(" ")
st.write(" ")
st.write("---") # Division Line
st.write("---") # Division Line

# ~~~~~~~~~~~~~~~~~~~~~~~~ Terms and Conditions ~~~~~~~~~~~~~~~~~~~~~~~~   
st.subheader("Terms and Conditions")
st.markdown('''
**Terms and Conditions**

Welcome to Aileana. By using our application, you agree to comply with and be bound by the following terms and conditions of use, which together with our privacy policy govern Aileana's relationship with you in relation to this application.

**Data Collection and Usage**

Aileana collects and stores only the user's email address and chat queries. This information is used solely for the purpose of analyzing user interactions and improving the features and services offered by the application. We are committed to ensuring that your privacy is protected. Should we ask you to provide certain information by which you can be identified when using this application, you can be assured that it will only be used in accordance with this privacy statement.

**User Consent**

By using Aileana, you consent to the collection and use of your email address and chat queries as described above. If you do not agree with these terms, please do not use our application.

**Changes to Terms**

Aileana reserves the right to change these terms and conditions at any time. Any changes will be posted on this page, and it is your responsibility to review these terms periodically to ensure you are aware of any updates.

**Contact Information**

If you have any questions about these terms and conditions, please contact us through LinkedIn [here](https://www.linkedin.com/in/dimitris-koutsomichalis).
''')

# ~~~~~~~~~~~~~~~~~~~~~~~~ Footer ~~~~~~~~~~~~~~~~~~~~~~~~   
st.write("---") # Division Line
st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")
