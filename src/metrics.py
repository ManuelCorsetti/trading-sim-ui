import numpy as np


def sharpe_ratio(returns, periods=12, risk_free_rate=0.0):
    """
    Calculate the Sharpe ratio for a given set of returns, adjusting for monthly data and annualizing.

    Parameters:
    - returns (pd.Series): Series of investment returns.

    Returns:
    - sharpe_ratio (float): The calculated Sharpe ratio, annualized.
    """
    excess_returns = returns - risk_free_rate
    avg_returns = excess_returns.rolling(
        window=periods
    ).mean()  ##todo: Update to use time instead of periods

    # Avoid division by zero
    stdev = excess_returns.rolling(window=periods).std()
    # replace stdev values of 0 with 0.0001 to avoid division by zero
    if (stdev == 0).any().any() > 0:
        stdev = stdev.replace(0, 0.0001)

        # raise an alert but not an error to tell the user that some stdev values are 0
        print("Warning: Some stdev values are 0 and have been replaced with 0.0001")

    # Annualize the Sharpe ratio
    annualized_sharpe_ratio = avg_returns / stdev
    return annualized_sharpe_ratio


def sortino_ratio(returns, risk_free_rate, target_return):
    """
    Calculate the Sortino ratio for a given set of returns.

    The Sortino ratio measures the risk-adjusted return of an investment
    by considering only the downside risk, which is the risk of returns
    falling below a specified target return.

    Parameters:
    returns (array-like): Array of returns.
    risk_free_rate (float): Risk-free rate of return.
    target_return (float): Target return.

    Returns:
    float: The Sortino ratio.

    Raises:
    None

    """
    downside_returns = np.where(returns < target_return, returns - target_return, 0)
    downside_std = np.std(downside_returns)

    if downside_std == 0:
        return np.nan

    sortino_ratio = (np.mean(returns) - risk_free_rate) / downside_std
    return sortino_ratio
