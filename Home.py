import streamlit as st
import pandas as pd
import numpy as np

from components.sidebar_auth import init_sidebar_auth

# Title 
st.title('Aileana')
# Subtitle
st.write(f'**Your job companion in Cyprus**')

#  ~~~~~~~~ User Email & Terms Acceptance ~~~~~~~~ 

# Initialize auth in sidebar
user_email = init_sidebar_auth()


#  ~~~~~~~~~~~~~~ Main Page Content ~~~~~~~~~~~~~~

# Description of Aileana Project in a Text Box
st.markdown('''
### **Welcome** 👋👋👋
Allow me to introduce you to Aileana, your personal career coach in Cyprus.\n
This is a passion project focused on exploring and analyzing data related to the job market of Cyprus.\n
It is also an opportunity to geek out on Artificial Intelligence and the capabilities of Large Language Models in data extraction, analysis, and classification.\n
''')


