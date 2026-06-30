from ollama import chat

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Explain Retrieval Augmented Generation like I'm an experienced software engineer."
        }
    ],
)

print(response["message"]["content"])