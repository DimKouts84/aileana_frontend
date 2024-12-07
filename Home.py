import streamlit as st
import pandas as pd
import numpy as np

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


#  ~~~~~~~~~~~~~~ Home Page Hero widget ~~~~~~~~~~~~~~
widgets.hero_section(
    title="Aileana",
    subtitle="👩‍💻 Your AI Occupational Analyst & Career Coach.",
)

st.write("---") # Division Line

# Description of Aileana Project in a Text Box
st.markdown('''
### **Welcome Traveler 👋 !**
This is a passion ⛃ data oriented project focused on exploring and analyzing data related to the job market [of Cyprus]. \n
It is also an opportunity to geek out on ✨ Artificial Intelligence and the capabilities of 🤖 Large Language Models in mainly on automated data extraction, analysis, and classification.\n
''')
st.write("\n")
st.write("\n")
st.write("\n")
st.write('''
### **What's the Secret Sauce 🧪?**
Aileana is not just a simple chatbot 🤖, the magic happens behind the scenes, where a framework of AI agents performs powerful operations on job postings:

- Data extraction and analysis
- Cleaning and classification of key parameters including:
  - Standardized Occupations & Job Titles 👔
  - Standardized Industries that require these jobs 🏭
  - Skills and Qualifications required 🛠️
  - Work Experience and Education Levels 🎓
  - Type of Employment (Full-time, Part-time, etc.) 🕒  
  - And other attributes hidden in unstructured text.
\n All of these stored into a Knowledge Graph Database to efficiently query and retrieve information.
\n You will be able to explore more on the how to in the [About](About) page and for more into the technical details of the process in the [Github](https://github.com/DimKouts84) page.
''')


st.write("---") # Division Line
# ~~~~~~~~~~~~~~~~~~~~~~~~ How to use information ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Aileana's main features
st.subheader("Main Features")
st.markdown('''
- **Occupational Analysis**: Aileana can help you understand the job market and the skills required for different roles.
- **Career Coaching**: Aileana can provide you with insights on how to navigate your career path.
- **Market Trends**: Aileana can keep you updated on the latest market trends.
''')

# Top Industries Treemap
st.caption("Data analysis & Insights example:") 
# st.write("Top 10 Industries by Number of Job Postings")
visualizations.top_industries_treemap()

st.write("---") # Division Line
# Aileana's main features
st.subheader("How to Use Aileana")
st.markdown('''
- **Everything in English**: All jobs are tranlated to english before being processed.
- **Select a Feature**: Choose a feature from the sidebar to start exploring.
- **Authenticate**: Login to access the full functionality of Aileana.
- **Interact**: Use the input fields to interact with Aileana.
''')

# Say enjoy to users 
st.write("---") # Division Line
st.caption("**Enjoy your journey with Aileana!** 🚀")
st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")