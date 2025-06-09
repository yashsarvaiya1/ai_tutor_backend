from fastapi import APIRouter,HTTPException
from schemas.chat_schema import ChatRequest,ChatResponse
from services.chat_service import chat_with_ai

router = APIRouter()

@router.post("/generate_chat",response_model=ChatResponse)
async def chat_with_genai(message_schema: ChatRequest):
    try:
        result = chat_with_ai(message= message_schema.message)
        return ChatResponse(response= result)
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))