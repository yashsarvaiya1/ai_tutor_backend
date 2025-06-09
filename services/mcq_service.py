from google import genai
from core.config import API_KEY
from schemas.mcq_schema import MCQResponse
import json
from google.genai import types

client = genai.Client(api_key=API_KEY)

def generate_mcqs(topic: str) -> MCQResponse:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Generate 5 multiple choice questions on the topic: {topic}",
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
            temperature=0.5,
            top_k=2,
            top_p=0.5,
            seed=42,
            max_output_tokens=1024
        )
    )

    raw = response.text.strip()
    parsed = json.loads(raw)
    return MCQResponse(**parsed)
