from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
    
app = FastAPI()

# 🔹 Middleware do CORS — żeby frontend mógł się łączyć
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()

    message = data.get("message")
    history = data.get("conversationHistory", [])

    reply = f"Odpowiedź z backendu na pytanie: '{message}'"

    return {
        "reply": reply,
        "received_history_length": len(history)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)