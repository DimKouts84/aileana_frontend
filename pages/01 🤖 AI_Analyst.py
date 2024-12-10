import streamlit as st
from components import sidebar_auth
from components import databases as db
from components import llm as llm

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

st.title("You AI Analyst and Career Coach")
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
            print(f"----User Question: \n{user_question}\n")
            # Save the query to the database (use timestamp)
            cipher_query = llm.query_to_data_engineer(llm.data_engineer_system_prompt, user_question, 0)
            if cipher_query == "NONE":
                print("---- No Cypher query needed for the question.\n")
                graph_data = "No job related information available"
            else:
                print(f"---- Cypher query:\n{cipher_query}.\n")
                graph_data = db.get_job_data_from_Cypher(cipher_query)
                # Save Query in database (use timestamp)
                print(f"---- Graph Data:\n{graph_data}\n")
            
            occupational_analyst_answer = llm.query_to_occupational_analyst(llm.occupational_analyst_system_prompt, user_question, graph_data, 0)
    
            st.write("🚀 Answer:")
            st.write(occupational_analyst_answer)
        else:
            st.warning("Please enter a question.")
    
    # Say enjoy to users 
    st.write("---") # Division Line
    st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")



