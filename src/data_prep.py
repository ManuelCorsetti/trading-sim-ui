import pandas as pd


def calculate_weights(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the normalized weights for each row in the DataFrame,
    setting negative values to 0 and normalizing so that each row sums to 1.

    Parameters:
    - data: A pandas DataFrame with numerical values.

    Returns:
    - A pandas DataFrame containing the normalized weights.
    """
    # Ensure non-negative values by clipping any negative values to zero in place
    data.clip(lower=0, inplace=True)

    # Normalize each row such that the row sums to 1
    row_sums = data.sum(axis=1)
    # Use .div() with broadcasting to divide each row by its corresponding sum

    data = data.div(row_sums, axis="index").fillna(
        0
    )  # fillna in case of division by zero

    return data
