import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

NEWS_API_KEY = "YOUR_NEWSAPI_KEY"  # Get free API key from https://newsapi.org/

def fetch_news_headlines(symbol):
    # Using NewsAPI - query company name or ticker symbol
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={symbol} AND India&"
        f"language=en&"
        f"sortBy=publishedAt&"
        f"apiKey={NEWS_API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    if data.get("status") != "ok":
        return []
    articles = data.get("articles", [])
    headlines = [article['title'] for article in articles if article.get('title')]
    return headlines[:10]  # top 10 recent headlines

def analyze_sentiment(headlines):
    analyzer = SentimentIntensityAnalyzer()
    if not headlines:
        return 0.0  # neutral if no news

    scores = [analyzer.polarity_scores(h)['compound'] for h in headlines]
    avg_score = sum(scores) / len(scores)
    return avg_score  # range -1 (neg) to +1 (pos)
