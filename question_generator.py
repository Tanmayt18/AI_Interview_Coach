from llm_engine import ask_llama

def generate_question(role, difficulty):

    prompt = f"""
You are a technical interviewer.

Ask ONE {difficulty} interview question for a {role} candidate.
Do not explain the answer.
"""

    return ask_llama(prompt)