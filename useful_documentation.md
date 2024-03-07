# Notes on `bt` Module
## [Algos](https://pmorissette.github.io/bt/algos.html)
### Debugging
The easiest way to debug algos is by adding leveraging one of the existing debug algos or by writing your own! Just insert them in the appropriate places in your algo stack, and add breakpoints to examine the state of the passed strategy.

`Debug`

`PrintTempData`

`PrintInfo`

`PrintRisk`

### Branching and Control Flow
While the Algo setup may seem overly simple (a list of functions which returns either True or False), this is a powerful construct that allows for complex branching and conditional structures. In particular, branching is achieved via the Or Algo.

For example, the code below illustrates how printing of strategy performance can occur on a different timeline from rebalancing the portfolio. Additional conditions can be added by placing those algos at the head of the relevant stack.

```python
import bt

data = bt.get('spy,agg', start='2010-01-01')

# create two separate algo stacks and combine the branches
logging_stack = bt.AlgoStack(
                    bt.algos.RunWeekly(),
                    bt.algos.PrintInfo('{name}:{now}. Value:{_value:0.0f}, Price:{_price:0.4f}')
                    )
trading_stack = bt.AlgoStack(
                    bt.algos.RunMonthly(),
                    bt.algos.SelectAll(),
                    bt.algos.WeighEqually(),
                    bt.algos.Rebalance()
                    )
branch_stack =  bt.AlgoStack(
                    # Upstream algos could go here...
                    bt.algos.Or( [ logging_stack, trading_stack ] )
                    # Downstream algos could go here...
                    )

s = bt.Strategy('strategy', branch_stack, ['spy', 'agg'])
t = bt.Backtest(s, data)
r = bt.run(t)
```