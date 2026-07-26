import numpy as np

def prices_to_log_returns(price_df):
    log_returns = np.log(price_df / price_df.shift(1))
    return log_returns.dropna(how="all")