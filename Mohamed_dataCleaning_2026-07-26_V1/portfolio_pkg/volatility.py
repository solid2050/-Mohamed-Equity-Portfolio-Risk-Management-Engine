import numpy as np

def rolling_volatility(return_series, window=21, annualize=True, trading_days=252):
    vol = return_series.rolling(window=window).std()
    if annualize:
        vol = vol * np.sqrt(trading_days)
    return vol.to_frame(name="rolling_volatility")