TICKERS = ["AAPL", "MSFT", "NVDA", "JPM", "XOM", "AMZN", "META", "GOOGL", "TSLA", "UNH"]

START_DATE = "2020-01-01"
END_DATE = "2025-12-31"

RAW_PRICE_PATH = "data/raw/adjusted_prices_raw.csv"
CLEAN_PRICE_PATH = "data/processed/clean_price_matrix.csv"
CLEAN_RETURN_PATH = "data/processed/clean_return_matrix.csv"
PORTFOLIO_RETURN_PATH = "data/processed/portfolio_return_series.csv"
ROLLING_VOL_PATH = "data/processed/rolling_volatility_series.csv"

WINSOR_LOWER = 0.01
WINSOR_UPPER = 0.01
STALE_WINDOW = 5
ROLLING_VOL_WINDOW = 21

# Example weights; must sum to 1
WEIGHTS = {
    "AAPL": 0.10,
    "MSFT": 0.10,
    "NVDA": 0.10,
    "JPM": 0.10,
    "XOM": 0.10,
    "AMZN": 0.10,
    "META": 0.10,
    "GOOGL": 0.10,
    "TSLA": 0.10,
    "UNH": 0.10
}