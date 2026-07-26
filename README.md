# Portfolio Risk Pipeline

This project downloads daily historical data from Yahoo Finance for:
AAPL, MSFT, NVDA, JPM, XOM, AMZN, META, GOOGL, TSLA, UNH

Period: 2020-01-01 to 2025-12-31

## Tasks
- Adjust prices for splits and dividends
- Align trading dates
- Handle missing values
- Remove stale prices
- Winsorize extreme return errors
- Convert prices to log returns
- Build weighted portfolio returns
- Compute rolling volatility

## Outputs
- Clean price matrix
- Clean return matrix
- Portfolio return series
- Rolling volatility series

## Install
```bash
pip install -r requirements.txt
```

## Run
```bash
python main.py
```
