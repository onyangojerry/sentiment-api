# app/model.py
from transformers import pipeline

# Load model once at startup
#sentiment_pipeline = pipeline("sentiment-analysis")
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    revision="714eb0f"
)


def predict_sentiment(text: str):
    result = sentiment_pipeline(text)[0]
    return {
        "sentiment": result["label"],
        "confidence": round(result["score"], 4)
    }
