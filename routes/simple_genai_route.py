from fastapi import APIRouter,HTTPException
from services.simple_prompt_service import ask_genai
from schemas.simple_prompt_schema import SimplePrompt,SimplePromptResponse
from core.global_store import username

router = APIRouter()

@router.post("/generate_guide",response_model= SimplePromptResponse)
async def askQuestion(request: SimplePrompt):
    try:
        print(username)
        result = ask_genai(request.prompt)
        return SimplePromptResponse(response= result)
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

