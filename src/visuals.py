import plotly.express as px
import pandas as pd

def plot_by_sector(df: pd.DataFrame):
    '''Bar chart: investments by sector'''

    return px.bar(
        df,
        x="Setor",
        y="Valor",
        color="Setor",
        barmode="group",
        title="Investimentos por Setor"
    )

def plot_over_time(df: pd.DataFrame):
    ''' Line chart: investments over time'''

    return px.line(
        df,
        x='Ano',
        y='Valor',
        color='Setor',
        markers=True,
        title='Evolução dos Investimentos ao Longo do Tempo'
    )

def plot_by_state(df: pd.DataFrame):
    '''Choropleth: investments by Brazilian state (UF)'''
    
    return px.choropleth(
        df,
        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson',
        locations='UF',
        featureidkey='properties.sigla',
        color='Valor',
        color_continuous_scale='Blues',
        scope='south america',
        title='Investimentos por Estado (UF)'
    )