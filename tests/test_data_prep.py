import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

# Assuming calculate_weights is defined in a module named 'weight_calculator'
from src.data_prep import calculate_weights


class TestCalculateWeights(unittest.TestCase):

    def test_all_positive(self):
        # All positive values should just be normalized
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

        expected_result = pd.DataFrame({"A": [0.25, 0.333333], "B": [0.75, 0.666667]})

        result = calculate_weights(df)
        assert_frame_equal(result, expected_result, atol=1e-6)

    def test_negative_values(self):
        # Negative values should be set to 0 before normalization
        df = pd.DataFrame({"A": [-1, 2], "B": [3, -4]})

        expected_result = pd.DataFrame({"A": [0.0, 1.0], "B": [1.0, 0.0]})

        result = calculate_weights(df)
        assert_frame_equal(result, expected_result, atol=1e-6)

    def test_all_zero_or_negative(self):
        # Rows with all zero or negative values should result in zeros
        df = pd.DataFrame({"A": [0, -1], "B": [-2, -3]})

        expected_result = pd.DataFrame({"A": [0.0, 0.0], "B": [0.0, 0.0]})

        result = calculate_weights(df)
        assert_frame_equal(result, expected_result, atol=1e-6)

    def test_empty_dataframe(self):
        # An empty DataFrame should return an empty DataFrame
        df = pd.DataFrame()
        expected_result = pd.DataFrame()

        result = calculate_weights(df)
        assert_frame_equal(result, expected_result)


if __name__ == "__main__":
    unittest.main()
