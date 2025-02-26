import plotly.express as px
from dataset import *

mapa_estado = px.scatter_geo(
    df_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False},
    title='Receita por Estado'
)

mapa_estado.update_geos(
    lataxis_range=[-35, 5], 
    lonaxis_range=[-75, -30]  
)

receita_estado = px.bar(
    df_estado.head(5),
    x='Local da compra',
    y='Preço',
    text_auto= True,
    title='Top 5 Receita por Estado',
)

receita_mensal = px.line(
    df_receita_mensal,
    x='Mês',
    y='Preço',
    markers= True,
    range_y=(0, df_receita_mensal.max()),
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal',
    labels={'Preço': 'Receita (R$)'}
)

receita_categoria = px.bar(
    df_receita_categoria.head(5),
    title='Top 5 Receita por Categoria',
    text_auto= True,
)
