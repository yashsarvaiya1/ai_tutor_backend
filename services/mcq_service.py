from random import Random
from google import genai
from core.config import API_KEY
from schemas.mcq_schema import MCQResponse
import json
from google.genai import types

client = genai.Client(api_key=API_KEY)

def generate_mcqs(topic: str) -> MCQResponse:
    variation_id = Random().randint(1, 9999)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""Generate 5 unique multiple choice questions on the topic: {topic}
                Do not reuse typical examples. Use creative and easy phrasing.
                Include this tag for variation: V{variation_id}
        """,
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are an MCQ generator that MUST return a valid JSON object with double quotes only. "
                "No explanation, no markdown, no code blocks. Format:\n"
                "{\n"
                "  \"questions\": [\n"
                "    {\n"
                "      \"question\": \"...\",\n"
                "      \"options\": [\"...\", \"...\", \"...\", \"...\"],\n"
                "      \"answer\": \"...\"\n"
                "    }\n"
                "  ]\n"
                "}\n"
                "Respond with ONLY valid JSON — no surrounding text."
            ),
            response_mime_type='application/json',
        )
    )

    raw = response.text.strip()
    parsed = json.loads(raw)
    return MCQResponse(**parsed)
