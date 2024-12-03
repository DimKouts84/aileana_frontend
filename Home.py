import streamlit as st
import pandas as pd
import numpy as np
import time, re

# Title 
st.title('Aileana')
# Subtitle
st.write(f'**Your job companion in Cyprus**')

#  ~~~~~~~~ User Email & Terms Acceptance ~~~~~~~~ 

# Initialize session state variables
if "email" not in st.session_state:
    st.session_state.email = ""
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Submit form function
def submit_form():
    st.session_state.email = st.session_state.email_input
    st.session_state.submitted = True

# Email validation function
def is_valid_email(email):
    # Simple email validation regex pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Submit form function
def submit_form():
    user_email = st.session_state.email_input
    terms_accepted = st.session_state.terms_accepted
    if not is_valid_email(user_email):
        st.sidebar.error("Please enter a valid email address.")
    elif not terms_accepted:
        st.sidebar.error("Please accept the terms and conditions.")
    else:
        st.session_state.email = user_email
        st.session_state.submitted = True

# Only show the form if it hasn't been submitted
if not st.session_state.submitted:
    st.warning(f"Hi there👋, please identify with your email to gain access!")
    with st.sidebar.form("email_form"):
        st.text_input("Enter your email:", key="email_input")
        st.checkbox("I accept the terms and conditions", key="terms_accepted")
        st.form_submit_button("Submit", on_click=submit_form)

# Say hello to the validated user that submitted the form
elif st.session_state.email:
    st.sidebar.success(f"Hi  **{st.session_state.email}** 👋 👋 👋")
