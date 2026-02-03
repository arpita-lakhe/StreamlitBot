import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini Chatbot")

# Configure Gemini API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Use supported model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(("You", user_input))

    response = model.generate_content(user_input)
    st.session_state.messages.append(("Bot", response.text))

# Display chat
for role, msg in st.session_state.messages:
    st.markdown(f"**{role}:** {msg}")
