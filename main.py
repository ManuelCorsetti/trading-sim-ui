import pandas as pd
import bt
import yfinance as yf
from src.metrics import sharpe_ratio
from src.strategy import create_weighted_balance_backtest, equal_weight_backtest

# Define variables
stocks = ['AAPL', 'GOOG']  # Define your stock symbols

# Fetch or simulate your `prices` DataFrame here
data = yf.download(stocks, start="2010-01-01", end="2024-01-01")
prices = data['Adj Close'].resample('MS').first()


# Calculate sharpe ratio for each stock
periods = 6
returns = prices.pct_change(periods=periods).dropna()
sharpe = sharpe_ratio(returns, periods=periods)
weight_input = sharpe.dropna()

print(weight_input.head())

# Filter prices by the stocks that have a sharpe ratio
data_input = prices.loc[weight_input.index.dropna()]

print(data_input.head())

s1 = create_weighted_balance_backtest(data_input, weight_input)
s_base = equal_weight_backtest(data_input)

# Running both strategies together
combined_result = bt.run(s1, s_base)

# Plotting cumulative returns to compare strategies
combined_result.plot(title='Strategy Comparison: Cumulative Returns')

# Displaying quantitative metrics
combined_result.display()

# For more detailed analysis, you can display and compare specific metrics like Sharpe Ratio, Max Drawdown, etc.
combined_result.display_lookback_returns()