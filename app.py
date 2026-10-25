import streamlit as st

st.set_page_config(page_title="Alsamad AI Chatbot", page_icon="🤖")

st.title("🤖 Alsamad AI Chatbot")
st.write("Welcome! Ask me a question.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    text = prompt.lower()

    if "hello" in text or "hi" in text:
        reply = "Hello bro! 👋 How can I help you?"
    elif "python" in text:
        reply = "Python is a programming language used in AI and machine learning."
    elif "ai" in text:
        reply = "AI means Artificial Intelligence. It helps computers perform intelligent tasks."
    elif "github" in text:
        reply = "GitHub is a platform for storing and sharing code."
    else:
        reply = "Interesting question! I'm a beginner chatbot. I'll become smarter as I learn more."

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.rerun()