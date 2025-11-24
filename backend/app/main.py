from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from starlette.concurrency import run_in_threadpool

from .llm import create_reply

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

    if not message:
        return Response("missing 'message' in request body", status_code=400, media_type="text/plain")

    try:
        assistant_text = await run_in_threadpool(create_reply, message, None, None)
    except Exception as exc:
        return Response(f"LLM request failed: {str(exc)}", status_code=500, media_type="text/plain")

    return {
        "reply": assistant_text,
        "received_history_length": len(history)
    }


@app.post("/chat_openai")
async def chat_openai(request: Request):
    payload = await request.json()
    message = payload.get("message")
    system_prompt = payload.get("systemPrompt")
    model = payload.get("model")

    if not message:
        return Response("missing 'message' in request body", status_code=400, media_type="text/plain")

    try:
        assistant_text = await run_in_threadpool(create_reply, message, system_prompt, model)
    except Exception as exc:
        return Response(f"LLM request failed: {str(exc)}", status_code=500, media_type="text/plain")

    return Response(assistant_text or "", media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)