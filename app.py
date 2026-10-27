  
import streamlit as st
import streamlit.components.v1 as components
from openai import OpenAI
from streamlit_mic_recorder import mic_recorder
import json

st.set_page_config(page_title="Nova AI", page_icon="🤖")

# Theme settings
with st.sidebar:
    st.title("🤖 Nova AI")
    theme = st.selectbox("🎨 Theme", ["Dark", "Light", "Purple"])
    speak = st.toggle("🔊 Speak replies", value=True)
    st.caption("Created by Alsamad")

colors = {
    "Dark": ("#080d1c", "#a9c7ff"),
    "Light": ("#f3f6ff", "#2857b8"),
    "Purple": ("#160821", "#df9cff")
}
bg, accent = colors[theme]

st.markdown(f"""
<style>
.stApp {{background:{bg};}}
.hero {{
 text-align:center; padding:22px; border-radius:22px;
 border:1px solid {accent};
 background:linear-gradient(135deg,#171a38,#30204b);
}}
.bot {{font-size:60px; animation:float 2s infinite ease-in-out;}}
@keyframes float {{
  0%,100% {{transform:translateY(0)}}
  50% {{transform:translateY(-9px)}}
}}
.hero h1 {{color:{accent};}}
div.stButton>button {{
 width:100%; border-radius:12px; border:1px solid {accent};
}}
</style>
<div class="hero">
 <div class="bot">🤖</div>
 <h1>Nova AI</h1>
 <p>Your Personal AI Buddy ✨</p>
 <p>Ask • Learn • Create</p>
</div>
""", unsafe_allow_html=True)

# Add OPENAI_API_KEY in Streamlit Secrets
key = st.secrets.get("OPENAI_API_KEY", "")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
         "content": "Hey Alsamad! 👋 I'm Nova. How can I help you?"}
    ]

def answer(prompt):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    if not key:
        reply = "🔑 Add your OpenAI API key in Streamlit Secrets to enable AI."
    else:
        try:
            client = OpenAI(api_key=key)
            result = client.responses.create(
                model="gpt-5.5",
                instructions=(
                    "You are Nova, a friendly AI buddy. "
                    "Help a CSE-AIML student using simple explanations."
                ),
                input=st.session_state.messages[-12:]
            )
            reply = result.output_text
        except Exception:
            reply = "Sorry! Check your API key, API access, and billing."

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    st.session_state.last_answer = reply

# Quick buttons
st.subheader("⚡ Quick Actions")
a, b = st.columns(2)

if a.button("🐍 Python"):
    answer("Teach me Python with an example.")
    st.rerun()

if b.button("🧠 AI/ML"):
    answer("Explain AI and machine learning.")
    st.rerun()

c, d = st.columns(2)

if c.button("💻 GitHub"):
    answer("Help me improve my GitHub portfolio.")
    st.rerun()

if d.button("🚀 Projects"):
    answer("Suggest three AI projects for beginners.")
    st.rerun()

# Display chat
st.subheader("💬 Chat with Nova")

for m in st.session_state.messages:
    with st.chat_message(
        m["role"],
        avatar="🤖" if m["role"] == "assistant" else "🧑"
    ):
        st.markdown(m["content"])

# Text input
prompt = st.chat_input("Message Nova...")

if prompt:
    answer(prompt)
    st.rerun()

# Voice input
st.subheader("🎤 Talk to Nova")

audio = mic_recorder(
    start_prompt="🎙️ Record",
    stop_prompt="⏹️ Stop",
    key="nova_voice"
)

if audio and audio.get("bytes") and st.button("Send voice"):
    if not key:
        st.warning("Configure your API key first.")
    else:
        try:
            import io
            client = OpenAI(api_key=key)
            f = io.BytesIO(audio["bytes"])
            f.name = "voice.webm"
            transcript = client.audio.transcriptions.create(
                model="gpt-4o-mini-transcribe", file=f
            )
            answer(transcript.text)
            st.rerun()
        except Exception:
            st.error("Voice input failed. Please try again.")

# Speak latest reply
if speak and st.session_state.get("last_answer"):
    components.html(
        "<script>"
        "const t = " +
        json.dumps(st.session_state["last_answer"]) + ";"
        "if ('speechSynthesis' in window) {"
        "speechSynthesis.cancel();"
        "speechSynthesis.speak(new SpeechSynthesisUtterance(t));"
        "}"
        "</script>",
        height=0
    )

if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.session_state.pop("last_answer", None)
    st.rerun()