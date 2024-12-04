import streamlit as st
from components import sidebar_auth, widgets, visualizations
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Aileana - Occupational Analyst & Career Coach",
    page_icon="👩‍💻",
    layout="centered",
    initial_sidebar_state="expanded",
)

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
### **Welcome Traveler** 👋
This is a passion ⛃ data oriented project focused on exploring and analyzing data related to the job market [of Cyprus]. \n
It is also an opportunity to geek out on ✨ Artificial Intelligence and the capabilities of 🤖 Large Language Models in mainly on automated data extraction, analysis, and classification.\n
''')

st.write("---") # Division Line
# ~~~~~~~~~~~~~~~~~~~~~~~~ Visualization ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Top Industries Treemap
visualizations.top_industries_treemap()

st.write("---") # Division Line
# ~~~~~~~~~~~~~~~~~~~~~~~~ Home Page Content ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Aileana's main features
st.subheader("Main Features")
st.markdown('''
- **Occupational Analysis**: Aileana can help you understand the job market and the skills required for different roles.
- **Career Coaching**: Aileana can provide you with insights on how to navigate your career path.
- **Market Trends**: Aileana can keep you updated on the latest market trends.
''')

st.write("---") # Division Line

# Aileana's main features
st.subheader("How to Use Aileana")
st.markdown('''
1. **Authenticate**: Login to access the full functionality of Aileana.
2. **Select a Feature**: Choose a feature from the sidebar to start exploring.
3. **Interact**: Use the input fields to interact with Aileana.
''')




