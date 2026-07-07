from fastapi import FastAPI
from pydantic import BaseModel
from ollama import chat

app = FastAPI(title="Enterprise AI Platform")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": request.message,
            }
        ],
    )

    return ChatResponse(
        response=response["message"]["content"]
    )