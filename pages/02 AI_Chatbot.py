import streamlit as st
from components.sidebar_auth import init_sidebar_auth


# Initialize auth in sidebar
user_email = init_sidebar_auth()


# Rest of your page code
if not user_email:
    # Show page content for authenticated users
    st.warning("Please login to access this page")
    st.write("Main content here")
else:
    st.write("Main content here")
    


