from pydantic import BaseModel, Field

class SimplePrompt(BaseModel):
    prompt: str = Field(..., description="The prompt to generate a response for user : ")
    max_tokens: int = Field(100, description="The maximum number of tokens to generate")
    
class SimplePromptResponse(BaseModel):
    response: str = Field(..., description="The generated response based on the prompt")
    