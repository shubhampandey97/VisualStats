# tests/test_data.py

from data.generator import generate_skewed_data

def test_data_size():
    data = generate_skewed_data(0)
    assert len(data) == 10_000

def test_reproducibility():
    d1 = generate_skewed_data(2)
    d2 = generate_skewed_data(2)
    assert (d1 == d2).all()
