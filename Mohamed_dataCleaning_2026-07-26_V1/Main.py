import os

from portfolio_pkg.config import (
    TICKERS, START_DATE, END_DATE,
    RAW_PRICE_PATH, CLEAN_PRICE_PATH, CLEAN_RETURN_PATH,
    PORTFOLIO_RETURN_PATH, ROLLING_VOL_PATH,
    WINSOR_LOWER, WINSOR_UPPER, STALE_WINDOW,
    ROLLING_VOL_WINDOW, WEIGHTS
)

from portfolio_pkg import (
    download_adjusted_prices,
    align_trading_dates,
    handle_missing_values,
    remove_stale_prices,
    winsorize_returns,
    prices_to_log_returns,
    build_weighted_portfolio_returns,
    rolling_volatility
)

def ensure_dirs():
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

def main():
    ensure_dirs()

    # 1) Download adjusted prices
    raw_prices = download_adjusted_prices(TICKERS, START_DATE, END_DATE)
    raw_prices.to_csv(RAW_PRICE_PATH)

    # 2) Align trading dates
    aligned_prices = align_trading_dates(raw_prices)

    # 3) Handle missing values
    filled_prices = handle_missing_values(aligned_prices)

    # 4) Remove stale prices
    clean_prices = remove_stale_prices(filled_prices, stale_window=STALE_WINDOW)
    clean_prices.to_csv(CLEAN_PRICE_PATH)

    # 5) Convert prices to log returns
    log_returns = prices_to_log_returns(clean_prices)

    # 6) Winsorize extreme return errors if needed
    clean_returns = winsorize_returns(
        log_returns,
        lower=WINSOR_LOWER,
        upper=WINSOR_UPPER
    )
    clean_returns.to_csv(CLEAN_RETURN_PATH)

    # 7) Build weighted portfolio returns
    portfolio_returns = build_weighted_portfolio_returns(clean_returns, WEIGHTS)
    portfolio_returns.to_csv(PORTFOLIO_RETURN_PATH)

    # 8) Rolling volatility series
    rolling_vol = rolling_volatility(
        portfolio_returns["portfolio_return"],
        window=ROLLING_VOL_WINDOW,
        annualize=True
    )
    rolling_vol.to_csv(ROLLING_VOL_PATH)

    print("Finished successfully.")
    print(f"Clean price matrix saved to: {CLEAN_PRICE_PATH}")
    print(f"Clean return matrix saved to: {CLEAN_RETURN_PATH}")
    print(f"Portfolio return series saved to: {PORTFOLIO_RETURN_PATH}")
    print(f"Rolling volatility saved to: {ROLLING_VOL_PATH}")

if __name__ == "__main__":
    main()