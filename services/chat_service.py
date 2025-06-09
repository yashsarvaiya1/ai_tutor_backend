from google import genai
from core.config import API_KEY
from google.genai import types

client = genai.Client(api_key=API_KEY)

chat =  client.chats.create(model="gemini-2.0-flash")

def chat_with_ai(message: str) -> str:
    result = chat.send_message(message=message)
    return result.text
