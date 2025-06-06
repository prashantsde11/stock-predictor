import pandas as pd

def add_indicators(df):
    df['SMA_5'] = df['Close'].rolling(window=5).mean()
    df['EMA_5'] = df['Close'].ewm(span=5, adjust=False).mean()
    df['Daily_Return'] = df['Close'].pct_change()
    return df




