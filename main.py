from fastapi import FastAPI
from dotenv import load_dotenv

from routes import chat_route, mcq_route, simple_genai_route , image_ai_route
from schemas.seruser_schema import SetUserRequest
from core import global_store 

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/setuser",response_model=SetUserRequest)
def setuser_data(response: SetUserRequest):
    global_store.username = response.username
    global_store.description = response.description
    return SetUserRequest(username=global_store.username,description=global_store.description)


@app.get("/getuser",response_model=SetUserRequest)
def getuser_data():
    return SetUserRequest(username=global_store.username,description=global_store.description)
    
    


app.include_router(chat_route.router,tags=["genai_chat"])
app.include_router(simple_genai_route.router,tags=["GENAI_SIMPLE"])
app.include_router(image_ai_route.router,tags=["image description"])
app.include_router(mcq_route.router,tags=["generate_mcq"])

