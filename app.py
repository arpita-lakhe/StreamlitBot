import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="StreamBot", page_icon="🤖")
st.title("🤖 Gemini Chatbot (Google AI Studio)")

# Configure API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("models/gemini-1.5-flash")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    response = st.session_state.chat.send_message(user_input)

    # Display conversation
    for msg in st.session_state.chat.history:
        role = "You" if msg.role == "user" else "Bot"
        st.markdown(f"**{role}:** {msg.parts[0].text}")
