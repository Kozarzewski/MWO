import os
from dotenv import load_dotenv
from openai import OpenAI

# Ładuje .env z katalogu uruchomienia (czyli MWO/backend)
load_dotenv()


def create_reply(message, system_prompt=None, model=None):
    if not message:
        raise RuntimeError("message is required")

    client = OpenAI()  # lokalny klient = bezpieczny w wątkach

    model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if system_prompt:
        prompt = f"System: {system_prompt}\n\nUser: {message}"
    else:
        prompt = message

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    # Bezpieczne wyciąganie tekstu z nowego SDK
    if hasattr(response, "output_text"):
        return response.output_text

    return str(response)
