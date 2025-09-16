import pandas as pd
import streamlit as st

@st.cache_data
def load_bndes_data(path: str) -> pd.DataFrame:
    """Load BNDES datasets from CSV or Excel"""
    if path.endswith('.csv'):
        df = pd.read_csv(path, sep=';')
    else:
        df = pd.read_excel(path)
    
    return df
