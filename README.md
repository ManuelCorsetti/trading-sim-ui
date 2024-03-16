# Trading Simulation UI
A **very** simple trading simulator environment in streamlit. It should allow a user to download a list of tickers to choose from, and from this allow the user to do the following:

1. Pick stocks
2. Pick value of each stock
3. Set trading start time
4. Trading end time
5. Visualize overall profits over period
6. Visualize final profits



# MVP
1. Use `bt` for backtesting
2. Use `alpaca` API for trade execution
   1. Start with paper trading for 3 months
3. Use `yfinance` for trading data
   1. Have created a local SQLite database with the trading data to avoid over-requesting (use for development)
4. Use `sqlite` database
   1. `SQLiteStudio` for SQL GUI

## 1. `bt` Trading Strategy

# Questions to Answer:
1. Where will you store the database?
# Future Considerations
- QantConnet's LEAN - For tracking trade strategies (investigate further as a platform)
  - QuantConnect as a platform only costs $8 per month - might be a viable long term solution with less maintenance
- `mlflow` for tracking experiments i.e. different strategies
  - It is meant for tracking ML strategies, but might be able to use to track trading strategies