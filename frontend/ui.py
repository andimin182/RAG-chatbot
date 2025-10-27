import streamlit as st
import requests

# -------------------------------
# Config
API_URL = "http://127.0.0.1:8000/query"  # Your FastAPI endpoint

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

st.title("🤖 Your job assistant")
st.write("Ask anything about your career")

# -------------------------------
# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------------
# User input
user_input = st.text_input("Your question:", key="input")

if st.button("Send") and user_input:
    # Call FastAPI
    try:
        response = requests.post(API_URL, json={"query": user_input})
        if response.status_code == 200:
            answer = response.json().get("answer")
        else:
            answer = f"Error {response.status_code}: {response.text}"
    except Exception as e:
        answer = f"Exception: {str(e)}"

    # Save to chat history
    st.session_state.history.append({"user": user_input, "bot": answer})

# -------------------------------
# Display chat history
for chat in reversed(st.session_state.history):
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")
