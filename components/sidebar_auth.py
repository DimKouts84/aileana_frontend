import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import os, psycopg2, re
from dotenv import load_dotenv

load_dotenv()

def init_sidebar_auth():
    # Initialize the cookie manager
    cookies = EncryptedCookieManager(
        prefix="", 
        password="your_secure_password"
    )

    if not cookies.ready():
        st.stop()

    # Initialize session state
    if "email" not in st.session_state:
        st.session_state.email = ""
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    def get_postresql_connection():
        return psycopg2.connect(
            host=os.getenv('POSTGRES_HOST'),
            database=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASS')
        )

    def insert_user(email):
        try:
            conn = get_postresql_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (email) VALUES (%s)", (email,))
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error inserting user: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()

    def is_valid_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

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
            cookies['user_email'] = user_email
            try:
                insert_user(user_email)
            except Exception as e:
                st.sidebar.error(f"Error creating user: {str(e)}")

    def logout():
        st.session_state.email = None
        st.session_state.submitted = False
        if 'user_email' in cookies:
            del cookies['user_email']
        st.rerun()

    # Render sidebar auth UI
    with st.sidebar:
        if 'user_email' in cookies:
            st.success(f"Hi {cookies['user_email']} 👋")
            st.button("Logout", on_click=logout)
        else:
            # st.warning("Please identify yourself")
            with st.form("email_form"):
                st.text_input("Enter your email:", key="email_input")
                st.checkbox("I accept the terms and conditions", key="terms_accepted")
                st.form_submit_button("Submit", on_click=submit_form)

    return cookies.get('user_email') if 'user_email' in cookies else None