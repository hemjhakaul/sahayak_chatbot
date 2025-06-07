import streamlit as st
import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key="xyz")

st.title("Welcome, I am Sahayak")

#  Initialize Gemini model (free version)
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

#  Initialize chat history and chat session
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.chat = model.start_chat(history=[])

#  Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Show user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get Gemini response
    response = st.session_state.chat.send_message(prompt)

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # Save assistant response to session
    st.session_state.messages.append({"role": "assistant", "content": response.text})

    #to run the code in the streamlit we run the command : streamlit run .\chatbot.py
