# data/generator.py

import numpy as np
from scipy.stats import skewnorm
import streamlit as st
from config.constants import DEFAULT_SAMPLE_SIZE, DEFAULT_RANDOM_SEED

@st.cache_data
def generate_skewed_data(skewness: float, size: int = DEFAULT_SAMPLE_SIZE):
    """
    Generate reproducible skewed data.
    """
    np.random.seed(DEFAULT_RANDOM_SEED)
    return skewnorm.rvs(a=skewness, size=size)
