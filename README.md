# 📈 stock-predictor

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A machine learning-based web API that predicts short-term trend (Bullish or Bearish) of Indian stocks—including penny stocks—based on stock technical indicators. Built using FastAPI, yfinance, and scikit-learn, with optional news-based sentiment.

---

## 🔗 Repository

**GitHub URL:** [https://github.com/prashantsde11/stock-predictor](https://github.com/prashantsde11/stock-predictor)

---

## 🚀 Features

- 📈 Predict stock trend (Bullish / Bearish)
- 🪙 Identify Penny Stocks (price < ₹10) and High-Value Stocks (price > ₹1000)
- 🧠 Basic ML-based prediction with confidence score
- 📰 (Optional) News sentiment stub support
- 🔗 Compatible with NSE (`.NS`) and BSE (`.BO`) stocks
- ⚡ FastAPI backend
- ✅ No paid API usage – uses open/free data only

---

## 🛠️ Tools & Technologies

- **Python 3.10+**
- **FastAPI** – Web API framework
- **pandas** – Data manipulation
- **numpy** – Numerical operations
- **yfinance** – Free stock market data (NSE/BSE)
- **scikit-learn** – Basic ML modeling
- **ta** – Technical indicators (RSI, MACD, etc.)
- **Uvicorn** – ASGI server for FastAPI

---

## 📁 Project Structure

```
stock-predictor/
│
├── app/
│   ├── main.py          # API route and logic
│   ├── predictor.py     # ML model for trend prediction
│   ├── features.py      # Technical indicator generator
│   ├── utils.py         # Helper for classification (penny, high-value)
│
├── requirements.txt     # Python packages
├── README.md            # Project documentation
```

---

## 📦 Installation Guide

1. **Clone the repository**
```bash
git clone https://github.com/prashantsde11/stock-predictor.git
cd stock-predictor
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the FastAPI server**
```bash
uvicorn app.main:app --reload
```

---

## 🧪 API Usage

### 📮 POST `/predict/`

Predicts the stock trend for a given BSE/NSE symbol and date.

**Request JSON**
```json
{
  "symbol": "TCS.NS",
  "date": "2025-05-30"
}
```

**cURL Example**
```bash
curl -X POST http://127.0.0.1:8000/predict/ \
-H "Content-Type: application/json" \
-d '{"symbol": "531137.BO", "date": "2025-06-02"}'
```

---

### ✅ Sample JSON Response

```json
{
  "symbol": "531137.BO",
  "date": "2025-06-02",
  "latest_price": 2.41,
  "stock_type": "Penny Stock",
  "prediction": "BEARISH",
  "confidence": {
    "bullish": 30.0,
    "bearish": 70.0
  },
  "suggestion": "SELL"
}
```

---

## 🔍 Symbol Format Guide

- Use `.NS` for **NSE** (e.g., `TCS.NS`, `RELIANCE.NS`)
- Use `.BO` for **BSE** (e.g., `531137.BO`, `500112.BO`)
- Penny stock: current price < ₹10
- High-value stock: current price > ₹1000

---

## 📂 requirements.txt

```txt
fastapi
uvicorn
pandas
numpy
scikit-learn
ta
yfinance
```

To get exact versions used:
```bash
pip freeze > requirements.txt
```

---

## 📄 Licensing

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more info.

---

## 🤝 Contributing

Feel free to fork the repo, improve, and raise a pull request.

---

## 🙋‍♂️ Author

**Prashant Mishra**  
GitHub: [@prashantsde11](https://github.com/prashantsde11)