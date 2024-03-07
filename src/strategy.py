import bt
import pandas as pd

# Assuming calculate_sharpe_ratio is defined somewhere
# from .metrics import sharpe_ratio

# Function to create and run the backtest
def create_weighted_balance_backtest(data_input, weights_input):
    # Create a strategy
    strategy = bt.Strategy('MonthlyRebalance', 
                           [bt.algos.RunMonthly(),  # Run the strategy monthly
                            bt.algos.SelectAll(),   # Use all data provided
                            bt.algos.WeighTarget(weights_input),  # Set target weights
                            bt.algos.Rebalance()])  # Rebalance to target weights

    # # Create a backtest object
    backtest = bt.Backtest(strategy, data_input)

    return backtest

# Function to create and run the baseline backtest with equal holdings
def equal_weight_backtest(data_input):
    # Define the strategy
    strategy = bt.Strategy('EqualWeight', 
                           [bt.algos.RunMonthly(),  # Run the strategy monthly
                            bt.algos.SelectAll(),   # Use all data provided
                            bt.algos.WeighEqually(),  # Assign equal weights to all assets
                            bt.algos.Rebalance()])  # Rebalance to target weights

    # Create a backtest object
    backtest = bt.Backtest(strategy, data_input)

    return backtest
