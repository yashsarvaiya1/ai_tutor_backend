from google import genai
from core.config import API_KEY
from core import global_store

client = genai.Client(api_key=API_KEY)

def ask_genai(prompt: str)-> str:
    result = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"prompt is {prompt} username is {global_store.username}"
    )
    return result.text