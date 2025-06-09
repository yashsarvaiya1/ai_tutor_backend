from pydantic import BaseModel
from typing import List

class MCQRequest(BaseModel):
    topic:str
    
class Question(BaseModel):
    question: str
    options: List[str]
    answer: str

class MCQResponse(BaseModel):
    questions: List[Question]