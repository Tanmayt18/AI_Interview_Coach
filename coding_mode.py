import streamlit as st
from streamlit_ace import st_ace
from llm_engine import ask_llama

def generate_coding_question():

    prompt = """
You are a technical interviewer.

Generate ONE DSA coding interview problem.

Return in this format:

Problem:
Description

Example Input:
Example Output:
"""

    return ask_llama(prompt)


def coding_editor():

    if "coding_question" not in st.session_state:
        st.session_state.coding_question = generate_coding_question()

    st.subheader("Coding Question")

    st.write(st.session_state.coding_question)

    st.subheader("Write Your Code")

    code = st_ace(
        language="python",
        theme="monokai",
        height=300
    )

    return code