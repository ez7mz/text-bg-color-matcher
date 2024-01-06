from cgitb import reset
from pyexpat import model
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils import ModelLoader
from contextlib import asynccontextmanager

class Message(BaseModel):
    hex: dict


ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["color_predictor"] = ModelLoader("./model/export/color_predictor_model.pth", "./model/data/color_dataset.csv")
    ml_models["color_predictor"].load_model()
    yield
    ml_models.clear()

app = FastAPI(lifespan=lifespan)

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
    r_value = color.hex['r']
    g_value = color.hex['g']
    b_value = color.hex['b']
    print(color)
    result = ml_models["color_predictor"].predict_text_color([r_value, g_value, b_value])
    if r_value == None or g_value == None or b_value == None:
        return {"result": "error"}
    elif result == 'white':
        return {"result": "#ffffff"}
    else:
        return {"result": "#000000"}
