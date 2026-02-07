import numpy as np
from core import dataset_manager as dm


def test_add_and_get_dataset():
    data = np.array([1, 2, 3])

    dm.add_dataset("test", data)

    assert dm.get_active_name() == "test"
    assert dm.get_active_dataset() is not None


def test_list_datasets():
    data = np.array([4, 5, 6])

    dm.add_dataset("another", data)

    names = dm.list_datasets()
    assert "another" in names


def test_set_active_dataset():
    data = np.array([7, 8, 9])

    dm.add_dataset("switch", data)
    dm.set_active_dataset("switch")

    assert dm.get_active_name() == "switch"
