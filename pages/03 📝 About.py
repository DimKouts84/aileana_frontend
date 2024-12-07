import streamlit as st
from components.sidebar_auth import init_sidebar_auth

# Page Configuration
st.set_page_config(
    page_title="About",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Initialize auth in sidebar
user_email = init_sidebar_auth()


st.subheader("About Aileana")
st.markdown('''

''')

st.subheader("Terms and Conditions")
st.markdown('''

''')
# Say enjoy to users 
st.write("---") # Division Line
st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")
