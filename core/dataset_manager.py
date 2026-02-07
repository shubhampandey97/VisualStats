"""
Dataset Manager

Handles:
- storing multiple datasets in Streamlit session
- switching active dataset
- retrieving dataset list

Pure logic wrapper around st.session_state.
"""

from typing import Dict, List, Optional
import streamlit as st


_DATASETS_KEY = "datasets"
_ACTIVE_KEY = "active_dataset"


def _ensure_initialized() -> None:
    """Initialize session storage if missing."""
    if _DATASETS_KEY not in st.session_state:
        st.session_state[_DATASETS_KEY] = {}

    if _ACTIVE_KEY not in st.session_state:
        st.session_state[_ACTIVE_KEY] = None


# ------------------------------------------------------------------
# Public API
# ------------------------------------------------------------------

def add_dataset(name: str, data) -> None:
    """Store dataset and set as active."""
    _ensure_initialized()

    st.session_state[_DATASETS_KEY][name] = data
    st.session_state[_ACTIVE_KEY] = name


def list_datasets() -> List[str]:
    """Return all dataset names."""
    _ensure_initialized()
    return list(st.session_state[_DATASETS_KEY].keys())


def get_active_dataset():
    """Return currently active dataset data."""
    _ensure_initialized()

    active = st.session_state[_ACTIVE_KEY]
    if active is None:
        return None

    return st.session_state[_DATASETS_KEY].get(active)


def get_active_name() -> Optional[str]:
    """Return active dataset name."""
    _ensure_initialized()
    return st.session_state[_ACTIVE_KEY]


def set_active_dataset(name: str) -> None:
    """Switch active dataset if it exists."""
    _ensure_initialized()

    if name in st.session_state[_DATASETS_KEY]:
        st.session_state[_ACTIVE_KEY] = name
