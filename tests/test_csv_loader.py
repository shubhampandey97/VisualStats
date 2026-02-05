import io
import numpy as np
import pytest

from data.csv_loader import load_numeric_column, CSVDataError


def test_valid_numeric_column():
    csv = io.StringIO(
        "value\n1\n2\n3\n4\n5\n"
    )
    result = load_numeric_column(csv, "value")
    assert isinstance(result, np.ndarray)
    assert result.tolist() == [1, 2, 3, 4, 5]


def test_missing_column():
    csv = io.StringIO("a\n1\n2\n")
    with pytest.raises(CSVDataError):
        load_numeric_column(csv, "value")


def test_non_numeric_column():
    csv = io.StringIO("value\na\nb\n")
    with pytest.raises(CSVDataError):
        load_numeric_column(csv, "value")
