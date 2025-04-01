# app/main.py
from fastapi import FastAPI
from app.model import predict_sentiment
from app.schemas import TextInput, SentimentOutput
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Classification API!"}


@app.post("/predict", response_model=SentimentOutput)
def get_sentiment(data: TextInput):
    logging.info(f"Received text: {data.text}")
    return predict_sentiment(data.text)
