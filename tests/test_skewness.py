# tests/test_skewness.py

from logic.skewness import get_skew_state

def test_symmetric():
    assert get_skew_state(0.0) == "symmetric"
    assert get_skew_state(0.3) == "symmetric"

def test_right_skew():
    assert get_skew_state(2.0) == "right"

def test_left_skew():
    assert get_skew_state(-2.5) == "left"
