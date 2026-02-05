import pandas as pd
import numpy as np


class CSVDataError(Exception):
    """Raised when CSV data is invalid."""


def load_numeric_column(file, column_name: str) -> np.ndarray:
    """
    Load a numeric column from a CSV file.

    Parameters
    ----------
    file : file-like
        Uploaded CSV file
    column_name : str
        Name of numeric column

    Returns
    -------
    np.ndarray
        Numeric data array
    """
    df = pd.read_csv(file)

    if column_name not in df.columns:
        raise CSVDataError(f"Column '{column_name}' not found")

    series = df[column_name]

    if not pd.api.types.is_numeric_dtype(series):
        raise CSVDataError(f"Column '{column_name}' is not numeric")

    return series.dropna().to_numpy()
