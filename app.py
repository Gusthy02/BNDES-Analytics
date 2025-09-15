import streamlit as st
from src.data_loader import load_bndes_data
from src.preprocess import clean_bndes_data
from src.visuals import plot_by_sector, plot_over_time, plot_by_state


# Configuração inicial
st.set_page_config(page_title="BNDES Data Analytics", layout="wide")
st.title("📊 Análise de Investimentos do BNDES")


# Carregar e processar dados
df = load_bndes_data("data/bndes.csv")
df = clean_bndes_data(df)

st.subheader("Pré-visualização dos dados")
st.dataframe(df.head())


# Filtros
anos = sorted(df["Ano"].dropna().unique())
setores = sorted(df["Setor"].dropna().unique())
ufs = sorted(df["UF"].dropna().unique())

ano = st.sidebar.multiselect("Selecione o ano", anos, default=anos[-1:])
setor = st.sidebar.multiselect("Selecione o setor", setores, default=setores[:3])
uf = st.sidebar.multiselect("Selecione a UF", ufs, default=ufs[:5])

df_filtered = df[
    (df["Ano"].isin(ano)) &
    (df["Setor"].isin(setor)) &
    (df["UF"].isin(uf))
]


# Visualizações
st.subheader("Investimentos por Setor")
st.plotly_chart(plot_by_sector(df_filtered), use_container_width=True)

st.subheader("Evolução Temporal dos Investimentos")
st.plotly_chart(plot_over_time(df_filtered), use_container_width=True)

st.subheader("Distribuição Geográfica dos Investimentos")
st.plotly_chart(plot_by_state(df_filtered), use_container_width=True)