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
CHATBOT_AVATAR = "🤖"

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

    # Initialize session state for messages
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    st.subheader("How can I help?")

    # Display chat history
    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            # User messages on the right
            with st.container():
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.empty()
                with col2:
                    st.markdown(
                        f"<div style='padding:20px; border-radius:15px; text-align:right; border: 2px solid darkgray;'>{USER_AVATAR} <b>{user_email}</b>: <br><br> {msg['message']}</div>",
                        unsafe_allow_html=True)
                    st.write(" ")
        else:
            # Bot messages on the left
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    # Start a single container div that will contain both message and plot
                    st.markdown(
                        f'''<div style='padding:20px; border-radius:15px; border: 2px solid darkgray;'>
                        {CHATBOT_AVATAR} <b>AI Analyst</b>: <br><br> 
                        {msg['message']}
                        </div>''', unsafe_allow_html=True)
                if 'figure' in msg:
                    # Display the plot
                    with col1:
                        st.plotly_chart(msg['figure'])
                    st.write(" ")
                with col2:
                    st.empty()
                    st.write(" ")
                    
    # User input with callback
    def handle_user_input():
        user_question = st.session_state.user_input
        if user_question:
            # Append user's message to messages
            st.session_state.messages.append({'role': 'user', 'message': user_question})

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

            # Generate visualization
            fig = llm.query_to_visualizations(
                llm.visualizations_system_prompt, user_question, graph_data, 0
            )

            # Append bot's response and figure to messages
            st.session_state.messages.append({'role': 'bot', 'message': occupational_analyst_answer, 'figure': fig})

            # Clear the input field
            st.session_state.user_input = ''
        else:
            st.warning("Please enter a question.")

    # Place the text input below the chat messages
    st.text_input(
        "Type your message here...",
        key='user_input',
        on_change=handle_user_input
    )

    # Say enjoy to users 
    st.write("---") # Division Line
    st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")


