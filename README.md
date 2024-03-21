# Trading Strategy

# Trading Strategy Project

## Order of Calculation Execution:

1. Import 20 years of the stock we want to calculate Sharpe value.
2. Store Sharpe for 20-N years of data in a dataframe.
3. Repeat for all S&P500 stocks.
4. Pick top 30 stocks where the correlation of the portfolio is less than the threshold.
5. Invest the stock according to the weights wanted (set all weights to begin with).
   - Show how much money is in cash vs invested in each stock as a simple % of value vertical bar chart ![Bar Chart](path/to/bar-chart-image.png).
6. Store the object & the json (possibly to table?) in a SQL database for ease of querying.
7. Emphasize the performance of the various strategies with special attention paid to the performance metrics:
   - Returns (%)
   - Drawdown (%)
   - Consistency of results over the years
   - Median yearly return
   - Volatility of the performance of the portfolio.

```
########## Choose the best 30 tickers
ticker_list = get_ticker_list()
sharpe = {}

for ticker in ticker_list:
   data = import_data(ticker)
   sharpe[ticker] = sharpe(data)

# create a function that will pick the maximum return combination of portfolio investments during the time period that have a correlation of less than the correlation threshold

final_tickers = pick_best_tickers(sharpe, correlation_threshold = 0.1)

########## backtest the strategy with the tickers selected
strategy = create_strategy(tickers, weights=sharpe)
strategy.run()

# visualize strategy performance

```

## Components

1. **Backtesting**
   - Utilize the `bt` library for backtesting trading strategies to evaluate their performance without risking actual capital.

2. **Trading Data**
   - `yfinance` to fetch real-time trading data for the stocks selected by the user. This data is crucial for simulating realistic trading scenarios and for backtesting strategies.

3. **Database Integration**
   - **Transition to BigQuery**: As the project scales, we will transition to using BigQuery as our primary database. This change will facilitate handling larger datasets more efficiently, enabling more complex analyses and simulations. BigQuery's robust data warehousing capabilities will improve the project's scalability and performance, particularly in processing and analyzing large volumes of trading data.

## Development Tools
- **Transition Plan**: Detailed documentation and support will be provided for the transition to BigQuery, ensuring a smooth migration process for all project data and functionalities.

# Questions to Answer:
1. Where will you store the database?
- `mlflow` for tracking experiments i.e. different strategies
  - It is meant for tracking ML strategies, but might be able to use to track trading strategies