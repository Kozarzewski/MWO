import os
from dotenv import load_dotenv
from openai import OpenAI

# Load `.env` from repository root (fallback to backend/.env)
file_dir = os.path.dirname(__file__)
repo_root = os.path.abspath(os.path.join(file_dir, "..", ".."))
repo_env = os.path.join(repo_root, ".env")
backend_env = os.path.join(os.path.abspath(os.path.join(file_dir, "..")), ".env")
env_path = repo_env if os.path.exists(repo_env) else backend_env
load_dotenv(env_path, override=True)

# Minimal OpenAI client usage; create_reply returns plain text
client = OpenAI()


def create_reply(message, system_prompt=None, model=None):
    if not message:
        raise RuntimeError("message is required")

    model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    prompt = message
    if system_prompt:
        # If system prompt provided, prepend it to the input
        prompt = f"System: {system_prompt}\n\nUser: {message}"

    response = client.responses.create(model=model, input=prompt)

    # Prefer output_text, fallback to common shapes
    output = getattr(response, "output_text", None)
    if not output:
        try:
            output = response["choices"][0]["message"]["content"]
        except Exception:
            output = str(response)

    return output
