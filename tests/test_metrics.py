import unittest
import numpy as np
from src.metrics import sortino_ratio

class TestSortinoRatio(unittest.TestCase):

    def test_sortino_ratio_returns_float(self):
        returns = [0.05, 0.02, -0.03, 0.04, -0.01]
        risk_free_rate = 0.02
        target_return = 0.0
        result = sortino_ratio(returns, risk_free_rate, target_return)
        self.assertIsInstance(result, float)

    def test_sortino_ratio_with_positive_returns(self):
        returns = [0.05, 0.02, 0.03, 0.04, 0.01]
        risk_free_rate = 0.02
        target_return = 0.0
        result = sortino_ratio(returns, risk_free_rate, target_return)
        self.assertAlmostEqual(result, 1.4142135623730951)

    def test_sortino_ratio_with_negative_returns(self):
        returns = [-0.05, -0.02, -0.03, -0.04, -0.01]
        risk_free_rate = 0.02
        target_return = 0.0
        result = sortino_ratio(returns, risk_free_rate, target_return)
        self.assertAlmostEqual(result, -1.4142135623730951)

    def test_sortino_ratio_with_mixed_returns(self):
        returns = [0.05, -0.02, 0.03, -0.04, 0.01]
        risk_free_rate = 0.02
        target_return = 0.0
        result = sortino_ratio(returns, risk_free_rate, target_return)
        self.assertAlmostEqual(result, 0.7071067811865476)

    def test_sortino_ratio_with_zero_downside_std(self):
        returns = [0.05, 0.02, 0.03, 0.04, 0.01]
        risk_free_rate = 0.02
        target_return = 0.1
        result = sortino_ratio(returns, risk_free_rate, target_return)
        self.assertTrue(np.isnan(result))

if __name__ == '__main__':
    unittest.main()