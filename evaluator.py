from llm_engine import ask_llama

def evaluate_answer(question, answer):

    prompt = f"""
You are a senior technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return:

Score (0-10)
Feedback
Correct answer
"""

    return ask_llama(prompt)