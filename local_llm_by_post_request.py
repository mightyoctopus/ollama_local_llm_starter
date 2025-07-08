### Basic example of running a local LLM (Llama3:2:latest) by POST request

import requests

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2:latest"

messages = [
    {"role": "system", "content": "You are known for being an excellent cultural adviser with a lot of experience in living in Korea and multiple countries around the world."},
    {"role": "user", "content": "What are pros and cons living in South Korea and under Korean culture?"}
]

payload = {
    "model": MODEL,
    "messages": messages,
    "stream": False,
}

response = requests.post(url=OLLAMA_API, headers=HEADERS, json=payload)

print("CONTENT: ", response.json()["message"]["content"])
