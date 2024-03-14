import unittest
import numpy as np
import pandas as pd
from src.metrics import sharpe_ratio


class TestSharpeRatio(unittest.TestCase):
    def setUp(self):
        # Create a simple returns series with a datetime index
        dates = pd.date_range(start="2020-01-01", periods=2, freq="M")
        self.returns = pd.Series([0, 1], index=dates)

    def test_basic_calculation(self):
        """Test the Sharpe ratio calculation with default parameters."""
        # Risk-free rate is 0, so it's just the mean of the returns divided by their standard deviation, annualized
        result = sharpe_ratio(self.returns, periods=2)
        expected = 0.7071

        self.assertAlmostEqual(result.iloc[1], expected, places=4)


# if __name__ == '__main__':
#     unittest.main()


if __name__ == "__main__":
    unittest.main()
