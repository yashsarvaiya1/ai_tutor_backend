from fastapi import APIRouter
from schemas.mcq_schema import MCQRequest,MCQResponse
from services.mcq_service import generate_mcqs

router = APIRouter()

@router.post("/generate_mcq",response_model=MCQResponse)
async def getMcq(request: MCQRequest):
    return generate_mcqs(request.topic)