import pandas as pd

def normalize_weights(weights_dict, columns):
    weights = pd.Series(weights_dict, dtype=float)
    weights = weights.reindex(columns)
    if weights.isna().any():
        missing = list(weights[weights.isna()].index)
        raise ValueError(f"Missing weights for tickers: {missing}")
    weights = weights / weights.sum()
    return weights

def build_weighted_portfolio_returns(return_df, weights_dict):
    weights = normalize_weights(weights_dict, return_df.columns)
    portfolio_returns = return_df.mul(weights, axis=1).sum(axis=1)
    return portfolio_returns.to_frame(name="portfolio_return")