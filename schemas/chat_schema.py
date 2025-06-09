from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(...,description="a message sent by user")
    
class ChatResponse(BaseModel):
    role: str = 'ai'
    response: str