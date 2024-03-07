import bt
import pandas as pd

# Assuming calculate_sharpe_ratio is defined somewhere
# from .metrics import sharpe_ratio

def create_strategy_weighted_balance(weights,  **kwargs):
    # calculate sharpe ratio of the stocks for every month. Apply the function once per month every month, setting the month start as the first and only day of the month
    # Code to 
    
    s = bt.Strategy('SharpeWeighted',
        [
            bt.algos.WeighTarget(weights=weights),
            bt.algos.Rebalance()    # Execute the rebalance
        ]
    )
    
    return s