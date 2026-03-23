import streamlit as st

from coding_mode import coding_editor
from evaluator import evaluate_answer
from question_generator import generate_question
from resume_parser import extract_resume_text
from voice import speak
from streamlit_autorefresh import st_autorefresh
st.set_page_config(page_title="AI Interview Coach", layout="wide")

st.title("🤖 AI Interview Coach PRO")

if "question" not in st.session_state:
    st.session_state.question = ""

if "score" not in st.session_state:
    st.session_state.score = 0

# Avatar
import os
import streamlit as st

image_path = "assets/interviewer.png"

try:
    if os.path.exists(image_path):
        st.image(image_path, width=120)
except:
    st.write("🤖 AI Interviewer")

# Role selection
role = st.selectbox(
    "Select Interview Role",
    ["Software Engineer", "Machine Learning Engineer", "Data Scientist"]
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

st.divider()

st.subheader("🎤 Auto AI Interview Mode (Question every 60 seconds)")

auto_mode = st.toggle("Start Automatic Interview")

if auto_mode:

    # refresh every 60 seconds
    count = st_autorefresh(interval=60000, key="auto_refresh")

    if count == 0 or "auto_question" not in st.session_state:
        st.session_state.auto_question = generate_question(role, difficulty)

    if count > 0:
        st.session_state.auto_question = generate_question(role, difficulty)

    question = st.session_state.auto_question

    st.markdown("### 🤖 Interviewer Question")
    st.write(question)

    # optional voice
    speak(question)

    user_answer = st.text_area("Your Answer", key="auto_answer")

    if st.button("Evaluate Auto Interview Answer"):

        feedback = evaluate_answer(question, user_answer)

        st.subheader("AI Feedback")
        st.write(feedback)

# Generate Question
if st.button("Generate Interview Question"):

    question = generate_question(role, difficulty)

    st.session_state.question = question

    speak(question)

# Show Question
if st.session_state.question:

    st.subheader("Interview Question")

    st.markdown(
        f"<div class='ai-bubble'>{st.session_state.question}</div>",
        unsafe_allow_html=True
    )

# Answer Input
answer = st.text_area("Your Answer", key="main_answer")

# Evaluate Answer
if st.button("Evaluate Answer"):

    if answer.strip() != "":

        feedback = evaluate_answer(
            st.session_state.question,
            answer
        )

        st.markdown(
            f"<div class='user-bubble'>{answer}</div>",
            unsafe_allow_html=True
        )

        st.subheader("AI Feedback")

        st.write(feedback)

        st.session_state.score += 1

# Score meter
st.subheader("Interview Progress")

st.progress(min(st.session_state.score / 10, 1.0))

st.write("Questions completed:", st.session_state.score)

# Coding Mode
st.divider()


st.subheader("💻 Coding Interview Mode")

if st.button("Generate Coding Question"):
    st.session_state.coding_question = None

code = coding_editor()

if st.button("Submit Code"):
    st.success("Code submitted successfully!")

# Resume Upload
st.divider()

st.subheader("📄 Resume Based Questions")

uploaded_resume = st.file_uploader("Upload Resume (PDF)")

if uploaded_resume:

    text = extract_resume_text(uploaded_resume)

    st.success("Resume parsed successfully!")

    st.write("Preview:")

    st.write(text[:500])