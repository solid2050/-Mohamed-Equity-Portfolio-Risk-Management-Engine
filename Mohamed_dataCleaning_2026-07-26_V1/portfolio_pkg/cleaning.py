import numpy as np
import pandas as pd
from scipy.stats.mstats import winsorize

def align_trading_dates(price_df):
    price_df = price_df.copy()
    price_df = price_df.sort_index()
    full_index = pd.date_range(price_df.index.min(), price_df.index.max(), freq="B")
    return price_df.reindex(full_index)

def handle_missing_values(price_df):
    df = price_df.copy()
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.ffill().bfill()
    return df

def detect_stale_prices(price_df, stale_window=5):
    df = price_df.copy()
    stale_mask = pd.DataFrame(False, index=df.index, columns=df.columns)

    for col in df.columns:
        same_as_prev = df[col].diff().fillna(0).eq(0)
        groups = (same_as_prev != same_as_prev.shift()).cumsum()
        run_lengths = same_as_prev.groupby(groups).transform("sum")
        stale_mask[col] = same_as_prev & (run_lengths >= stale_window)

    return stale_mask

def remove_stale_prices(price_df, stale_window=5):
    df = price_df.copy()
    stale_mask = detect_stale_prices(df, stale_window=stale_window)
    df[stale_mask] = np.nan
    df = df.ffill().bfill()
    return df

def winsorize_returns(return_df, lower=0.01, upper=0.01):
    df = return_df.copy()
    for col in df.columns:
        s = df[col].dropna()
        if len(s) > 0:
            w = winsorize(s, limits=(lower, upper))
            df.loc[s.index, col] = np.asarray(w)
    return df