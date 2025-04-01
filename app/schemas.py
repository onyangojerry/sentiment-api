# app/schemas.py
from pydantic import BaseModel, Field

class TextInput(BaseModel):
    text: str = Field(..., min_length=1, description="Text to analyze")

class SentimentOutput(BaseModel):
    sentiment: str
    confidence: float
