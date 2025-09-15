import pandas as pd
import streamlit as at

@st.cache_data
def load_bndes_data(path: str) -> pd.DataFrame:
    ''' Load BNDES datasets from CSV or Excel'''
    if path.endswith('.csv'):
        df = df.read_csv(path, sep=';')
    else:
        df = df.read_excel(path)

    return df