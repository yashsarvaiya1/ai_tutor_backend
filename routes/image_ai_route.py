from fastapi import APIRouter,HTTPException,File,UploadFile
from schemas.image_ai import ImageDescribeResponse
from services.image_ai_service import describe_image

router  = APIRouter()

@router.post("/describe",response_model=ImageDescribeResponse)
async def get_description(file: UploadFile = File()):
    file_data = await file.read()
    description = describe_image(file_data)
    return ImageDescribeResponse(description=description)
 
    