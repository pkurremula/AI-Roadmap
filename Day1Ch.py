from ollama import chat

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "What is an embedding?"
        }
    ],
)

print(response["message"]["content"])

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "What is a token?"
        }
    ],
)

print(response["message"]["content"])

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "What is RAG?"
        }
    ],
)

print(response["message"]["content"])

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "What is an AI Agent??"
        }
    ],
)

print(response["message"]["content"])

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "What is MCP?"
        }
    ],
)

print(response["message"]["content"])