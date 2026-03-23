import requests

def ask_llama(prompt):

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)

    try:
        return response.json()["response"]
    except:
        return "AI response error. Make sure Ollama is running."