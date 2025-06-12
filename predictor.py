# predictor.py

import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol, start_date, end_date):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(start=start_date, end=end_date)
    return hist

def add_indicators(df):
    # Add simple moving average as an example indicator
    df['SMA_5'] = df['Close'].rolling(window=5).mean()
    df['SMA_10'] = df['Close'].rolling(window=10).mean()
    return df.dropna()

def classify_stock_price(price):
    if price < 10:
        return "Penny Stock"
    elif price > 1000:
        return "High-Value Stock"
    else:
        return "Mid-range Stock"

def simple_trend_prediction(df):
    # Simple example: if 5-day SMA > 10-day SMA then bullish else bearish
    last_row = df.iloc[-1]
    if last_row['SMA_5'] > last_row['SMA_10']:
        return "BULLISH", 0.7, 0.3  # 70% bullish confidence
    else:
        return "BEARISH", 0.3, 0.7  # 70% bearish confidence

def predict_stock_trend(symbol, date):
    # Fetch past 30 days data ending at date for indicators
    df = fetch_stock_data(symbol, start_date='2025-04-01', end_date=date)
    if df.empty or 'Close' not in df:
        return {"error": "No data found for symbol or date."}

    df = add_indicators(df)
    if df.empty:
        return {"error": "Not enough data to compute indicators."}

    latest_price = df['Close'].iloc[-1]
    stock_type = classify_stock_price(latest_price)
    prediction, bullish_conf, bearish_conf = simple_trend_prediction(df)

    suggestion = "BUY" if prediction == "BULLISH" else "SELL"

    return {
        "symbol": symbol,
        "date": date,
        "latest_price": latest_price,
        "stock_type": stock_type,
        "prediction": prediction,
        "confidence": {
            "bullish": bullish_conf * 100,
            "bearish": bearish_conf * 100,
        },
        "suggestion": suggestion,
    }


def classify_stock(symbol: str) -> str:
    try:
        stock = yf.Ticker(symbol)
        price = stock.history(period='1d')['Close'].iloc[-1]
        if price < 10:
            return "Penny Stock"
        elif price > 1000:
            return "High-Value Stock"
        else:
            return "Mid-range Stock"
    except Exception as e:
        return f"Error: {e}"