### Basic example of running a local LLM (Llama3:2:latest) by ollama SDK

import ollama

MODEL = "llama3.2:latest"

messages = [
    {"role": "system", "content": "You are known for being an excellent cultural adviser with a lot of experience in living in Korea and multiple countries around the world."},
    {"role": "user", "content": "What are pros and cons living in South Korea and under Korean culture?"}
]

response = ollama.chat(model=MODEL, messages=messages)
print(response["message"]["role"])
print(response["message"]["content"])





