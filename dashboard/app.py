import streamlit as st
import plotly.express as px
from dataset import *
from graficos import *
from utils import *


st.set_page_config(layout='wide')
st.title('Dashboard de Vendas :shopping_trolley:')
st.sidebar.title('Filtro de Vendedores')
filtro_vendedor = st.sidebar.multiselect(
    'Vendedor', 
    df['Vendedor'].unique())

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
with aba1:
    st.dataframe(df_total)
with aba2: 
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', formatar_numero (df['Preço'].sum(), 'R$'))
        st.plotly_chart(mapa_estado, use_container_width=True)
        st.plotly_chart(receita_estado, use_container_width=True)
    with coluna2: 
        st.metric("Quantidade de Vendas", formatar_numero(df.shape[0]))
        st.plotly_chart(receita_mensal, use_container_width=True)
        st.plotly_chart(receita_categoria, use_container_width=True)

with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(receita_vendedor)
    with coluna2:
        st.plotly_chart(vendas_vendedor)