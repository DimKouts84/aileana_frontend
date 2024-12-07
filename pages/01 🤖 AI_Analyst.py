import streamlit as st
from components import sidebar_auth
from components import databases as db


# Page Configuration
st.set_page_config(
    page_title="AI Analyst",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

USER_AVATAR = "🙋🏻‍♂️"
CHATBOT_AVATAR = "😎"

# Initialize auth in sidebar
user_email = sidebar_auth.init_sidebar_auth()

st.title("You personal AI Analyst")
st.write("An advanced LLM chatbot with a comprehensive understanding of the job market, designed to help individuals navigate their career paths and keep professionals updated on the latest market trends.")


st.write("---")

# Check if user is authenticated or not
# If not authenticated, show a warning message
if not user_email:
    # Show page content for authenticated users
    st.warning("Please login to access this page")
    
    # Say enjoy to users 
    st.write("---") # Division Line
    st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")
    
    st.stop()
    
# If user is authenticated
# Show the chatbot interface
elif user_email:

    # Chatbot interface
    st.subheader("How can I help?")
    user_question = st.text_input("Ask a question:")
    if st.button("Submit"):
        if user_question:
            answer = db.query_to_data_analyst(user_question)
            st.write("🚀 Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question.")
    
    # Say enjoy to users 
    st.write("---") # Division Line
    st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")



