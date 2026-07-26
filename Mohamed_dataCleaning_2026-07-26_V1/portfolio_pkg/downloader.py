import pandas as pd
import yfinance as yf

def download_adjusted_prices(tickers, start_date, end_date):
    df = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        auto_adjust=False,
        progress=False,
        actions=False
    )

    if isinstance(df.columns, pd.MultiIndex):
        if "Adj Close" in df.columns.get_level_values(0):
            prices = df["Adj Close"].copy()
        else:
            prices = df["Close"].copy()
    else:
        prices = df[["Adj Close"]].copy()
        prices.columns = tickers[:1]

    prices = prices.sort_index()
    prices.index = pd.to_datetime(prices.index)
    return prices