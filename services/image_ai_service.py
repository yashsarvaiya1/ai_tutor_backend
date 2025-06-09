from google import genai
from PIL import Image
from core.config import API_KEY
import tempfile

client = genai.Client(api_key=API_KEY)

def describe_image(file_data: bytes)-> str:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".jpg") as tmp:
        tmp.write(file_data)
        tmp_path = tmp.name
    
    image = Image.open(tmp_path)
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            "Describe this image clearly and consicely with at least two details in one paragraph.",
            image
        ]
    )
    
    return response.text