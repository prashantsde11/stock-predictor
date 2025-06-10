from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from datetime import datetime
from app.predictor import predict_stock_trend, classify_stock



app = FastAPI()

class PredictRequest(BaseModel):
    symbol: str
    date: str  # Format YYYY-MM-DD

@app.post("/predict/")
async def predict(request: PredictRequest):
    result = predict_stock_trend(request.symbol, request.date)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result



@app.get("/classify/")
def classify(symbol: str = Query(..., description="Stock symbol e.g. 531137.BO or TCS.NS")):
    classification = classify_stock(symbol)
    return {
        "symbol": symbol,
        "classification": classification
    }

