import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Aileana - Occupational Analyst & Career Coach",
    page_icon="👩‍💻",
    layout="centered",
    initial_sidebar_state="expanded",
)

from components import sidebar_auth, widgets, visualizations


#  ~~~~~~~~ Sidebar ~~~~~~~~ 
# Initialize auth in sidebar
user_email = sidebar_auth.init_sidebar_auth()

#  ~~~~~~~~~~~~~~ Home Page Top Section ~~~~~~~~~~~~~~
# widgets.top_logo_section()

widgets.hero_section(
    title= "AILEANA",
    subtitle=" Let the job market tell you a story 📖",
)
    

st.write("---") # Division Line

# Description of Aileana Project in a Text Box
st.markdown('''
### **Welcome Traveler !**
This is a passion ⛃ data oriented project focused on exploring and analyzing data related to the job market [of Cyprus]. \n
It is also an opportunity to geek out on ✨ Artificial Intelligence and the capabilities of 🤖 Large Language Models in mainly on automated data extraction, analysis, and classification.\n
''')

# Some space between Paragraphs
st.write(" ")
st.write(" ")
st.write(" ")


st.write('''
#### **What's the Secret Sauce?**
Aileana is not just a simple dashboard with charts or a chatbot, the magic 🧪 happens behind the scenes, where a custom agentic framework of LLMs perform powerful operations on the unstructured text of job postings.
''')

# Some space between Paragraphs
st.write(" ")
st.write(" ")
st.write(" ")


st.write('''
##### Chatbot interface for user interaction
- Chating with an AI Analyst & Career Coach. A series of AI agents are used to provide the user with the information they need.
  - **Text to database queries**: Based on user's request AI automated queries are made to the database for relevant information using RAG (Retrieval Augmented Generation) method.
  - **Analysis of Context**: An AI agent combines the database data and the user's question, to provide a comprehensive analysis to the user.
  - **Automated Graphs**: When possible another agents creates a graph related to the user's request.

''')

# Some space between Paragraphs
st.write(" ")
st.write(" ")
st.write(" ")


st.write('''
##### Data Processing from job postings
- Data extraction and analysis
- Cleaning and classification of key parameters including:
  - Standardized Occupations & Job Titles 👔
  - Standardized Industries that require these jobs 🏭
  - Skills and Qualifications required 🛠️
  - Work Experience and Education Levels 🎓
  - Type of Employment (Full-time, Part-time, etc.) 🕒  
  - And other attributes hidden in unstructured text.
  
All of these stored into a Knowledge Graph Database to efficiently query and retrieve information.

You will be able to explore more on the how to in the [About](About) page and for more into the technical details of the process in the [Github](https://github.com/DimKouts84) page.
''')


# ~~~~~~~~~~~~~~~~~~~~~~~~ How to use information ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

st.write("---") # Division Line
st.write(" ")
st.write(" ")

# Top Industries Treemap
st.write("##### Data Analysis, Insights and Examples 📊")

st.write('''
**The Secret Weapon 🛡️**
For a high level overview of the tech behind the scenes, the power of _GenAI_ and _LLMs_ seem the way to go. However the real magic happens in the :blue[Knowledge Graph Database].

Below is a visual representation on how powerful the Knowledge Graph Database can be, by creating the appropriate nodes and relationships, of only 300 Jobs and 3.900 Total Nodes related to each other.
''')

with open('static/knowledge_graph_visualisation_300_job_and_3900_total_nods.png', 'rb') as f:
    graph_visualization = f.read()
    
st.image(graph_visualization, caption="The colored nodes represent different entity types (jobs, skills, industries, etc.), while the edges show their relationships.")

st.write("---") # Division Line

visualizations.top_job_titles_and_skils_sunburst()
st.write(" ")
visualizations.top_industries_treemap()

st.write("> Please, enjoy your journey with ✨ :blue[**Aileana**] and feel free go throught the rest of the pages to explore more about the project.")

# ~~~~~~~~~~~~~~~~~~~~~~~~ Footer ~~~~~~~~~~~~~~~~~~~~~~~~   
st.write("---") # Division Line
st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")
