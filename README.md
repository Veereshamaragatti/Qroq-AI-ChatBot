# Groq Chatbot with Streamlit and ngrok 🚀

This project creates a chatbot web application using **Streamlit**, powered by **Groq API**, and hosted publicly via **ngrok**. The chatbot leverages the \`llama-3.3-70b-versatile\` model to generate intelligent responses to user queries.

## Features
- **Interactive Chat Interface:** Ask questions and get AI-generated responses in real-time.
- **Persistent Chat History:** Maintains conversation history throughout the session.
- **Groq API Integration:** Utilizes Groq for advanced AI response generation.
- **Public Access via ngrok:** Exposes the app to the web with a public URL.

## Setup Instructions
1. Clone this repository.
2. Install the required dependencies:
   \`\`\`bash
   pip install streamlit groq pyngrok
   \`\`\`
3. Add your Groq API key:
   \`\`\`python
   api_key = \"your_groq_api_key\"
   \`\`\`
4. Set up ngrok with your authentication token:
   \`\`\`python
   ngrok.set_auth_token(\"your_ngrok_authtoken\")
   \`\`\`
5. Run the app:
   \`\`\`bash
   streamlit run app.py
   \`\`\`
6. Access the app through the public URL provided by ngrok.

## Requirements
- Python 3.7+
- Streamlit
- Groq
- pyngrok"
