api_key = "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"
import streamlit as st
from groq import Groq
from pyngrok import ngrok

# --- API Key Configuration ---
api_key = "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"
client = Groq(api_key=api_key)

# Page Configuration
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Groq Chatbot")
st.write("Ask me anything and I'll respond using Groq's API!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Interface
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(message["content"])

# User Input
user_input = st.chat_input("Enter your question here...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get Response from Groq API
    with st.spinner("Thinking..."):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": user_input}],
                model="llama-3.3-70b-versatile",
            )
            response = chat_completion.choices[0].message.content
        except Exception as e:
            response = f"An error occurred: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

import os

# Kill any existing Streamlit process
os.system("killall streamlit")

# Run Streamlit app
#streamlit run app.py &>/content/logs.txt &

# Get your ngrok authtoken from https://dashboard.ngrok.com/auth
# and replace 'YOUR_AUTHTOKEN' below
#ngrok.set_auth_token("YOUR_ACTUAL_AUTHTOKEN")  # Set your ngrok authtoken # Replace YOUR_AUTHTOKEN with your actual authtoken
ngrok.set_auth_token("2rtHivJ1UrOSKpVwXEHySV8S3Wh_4aRSqWbMK3cpBMYzE96fC") # Replace with your actual authtoken

# Expose the Streamlit app via ngrok
from pyngrok import ngrok

# Open a ngrok tunnel to the Streamlit app
public_url = ngrok.connect(8501)
print(f" * Streamlit app is live at: {public_url}")
