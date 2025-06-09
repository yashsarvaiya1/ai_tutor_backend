from pydantic import BaseModel

class SetUserRequest(BaseModel):
    username: str
    description: str
