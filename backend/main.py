from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class Message(BaseModel):
    color: dict

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/")
async def read_root():
    return {"message": "Hello World from the API"}

@app.post("/api/v1/predict/")
async def predict(color: Message):
    return {"message": f"You sent: {color}"}