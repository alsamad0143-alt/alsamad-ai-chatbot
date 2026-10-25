import streamlit as st

st.set_page_config(
    page_title="Nova AI | Your AI Buddy",
    page_icon="🤖",
    layout="centered"
)

# Custom design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #080d1c, #15102b);
    color: white;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
}

.hero {
    background: linear-gradient(135deg, #24205a, #102b48);
    padding: 25px;
    border-radius: 22px;
    text-align: center;
    border: 1px solid #5146a5;
    margin-bottom: 25px;
}

.robot {
    font-size: 65px;
}

.hero h1 {
    color: #a9c7ff;
    margin-bottom: 5px;
}

.hero p {
    color: #d6d9ff;
}

div.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #6558c9;
    background: #201b40;
    color: white;
    min-height: 45px;
}

div.stButton > button:hover {
    background: #44358b;
    color: white;
    border-color: #a9c7ff;
}

[data-testid="stChatMessage"] {
    border-radius: 15px;
    border: 1px solid #302b50;
}

[data-testid="stChatInput"] {
    border-color: #6558c9;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# Header and character
st.markdown("""
<div class="hero">
    <div class="robot">🤖</div>
    <h1>Nova AI</h1>
    <p>Your Personal AI Buddy ✨</p>
    <p>Ask questions • Learn coding • Explore AI</p>
</div>
""", unsafe_allow_html=True)


# Helpful chatbot responses
def get_reply(message):
    text = message.lower().strip()

    if any(word in text for word in [
        "hello", "hi", "hey", "hii"
    ]):
        return (
            "Hey there! 👋 I'm Nova, your AI buddy! "
            "What would you like to learn today? 🚀"
        )

    elif "python" in text:
        return (
            "🐍 Let's learn Python!\n\n"
            "Python is a programming language used in AI, "
            "machine learning, automation, and web development.\n\n"
            "Start with variables, data types, conditions, "
            "loops, functions, and lists."
        )

    elif "machine learning" in text or "aiml" in text:
        return (
            "🧠 Machine learning helps computers learn patterns "
            "from data and make predictions.\n\n"
            "Your learning path:\n"
            "1. Python\n"
            "2. NumPy and pandas\n"
            "3. Machine learning algorithms\n"
            "4. Model training and evaluation\n"
            "5. Build projects!"
        )

    elif "github" in text:
        return (
            "💻 GitHub is a platform for storing and sharing code.\n\n"
            "You can upload projects, track changes, collaborate "
            "with others, and build your developer portfolio."
        )

    elif "project" in text:
        return (
            "🚀 Here are some beginner project ideas:\n\n"
            "1. AI Chatbot\n"
            "2. Student Performance Predictor\n"
            "3. Movie Recommendation System\n"
            "4. Spam Message Detector\n"
            "5. Personal Portfolio Website\n\n"
            "Start small and improve your project step by step!"
        )

    elif "help" in text:
        return (
            "Of course! 💙 I'm here to help.\n\n"
            "You can ask me about Python, AI/ML, GitHub, "
            "coding, or project ideas. Tell me what you need!"
        )

    elif "who are you" in text or "your name" in text:
        return (
            "I'm Nova AI 🤖, your friendly digital buddy! "
            "I'm here to help you learn, explore coding, "
            "and discover new project ideas."
        )

    else:
        return (
            "💙 That's an interesting question!\n\n"
            "I'm currently running in starter mode, so I can "
            "answer a limited set of questions. You can ask "
            "me about Python, AI/ML, GitHub, or projects.\n\n"
            "Later, we can connect a real AI model to make "
            "me much smarter! ✨"
        )


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hey! 👋 I'm Nova, your AI buddy. "
                "Choose a button below or type your question!"
            )
        }
    ]


# Quick-action buttons
st.subheader("⚡ Quick Actions")

col1, col2 = st.columns(2)

with col1:
    python_button = st.button("🐍 Learn Python")
    ai_button = st.button("🧠 Explore AI/ML")

with col2:
    project_button = st.button("🚀 Project Ideas")
    github_button = st.button("💻 GitHub Help")


# Process selected button
quick_prompt = None

if python_button:
    quick_prompt = "Teach me Python"

elif ai_button:
    quick_prompt = "Explain machine learning"

elif project_button:
    quick_prompt = "Give me beginner project ideas"

elif github_button:
    quick_prompt = "Explain GitHub"


# Display chat history
st.subheader("💬 Chat with Nova")

for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "🧑"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


# User input
typed_prompt = st.chat_input("Message Nova...")

prompt = quick_prompt or typed_prompt

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    reply = get_reply(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()


# Footer controls
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.caption("✨ Made with Python and Streamlit")

with col2:
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.rerun()