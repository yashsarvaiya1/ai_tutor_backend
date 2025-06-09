from pydantic import BaseModel

class ImageDescribeResponse(BaseModel):
    description: str