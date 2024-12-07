import streamlit as st
from components import sidebar_auth

# Page Configuration
st.set_page_config(
    page_title="AI Analyst",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Initialize auth in sidebar
user_email = sidebar_auth.init_sidebar_auth()

# Rest of your page code
if not user_email:
    # Show page content for authenticated users
    st.warning("Please login to access this page")
    
    # Say enjoy to users 
    st.write("---") # Division Line
    st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")
    
    st.stop()
elif user_email:
    st.write("An advanced LLM chatbot with a comprehensive understanding of the job market, designed to help individuals navigate their career paths and keep professionals updated on the latest market trends.")

    
    # Say enjoy to users 
    st.write("---") # Division Line
    st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")
    


