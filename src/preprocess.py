import pandas as pd

def clean_bndes_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning and renaming of columns"""
    
    df.columns = df.columns.str.strip()
    
    df = df.rename(columns={
        'ano': 'Ano',
        'setor': 'Setor',
        'uf': 'UF',
        'valor': 'Valor'
    })

    df['Ano'] = df['Ano'].astype(int)
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce').fillna(0)

    return df
