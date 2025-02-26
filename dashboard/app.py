import streamlit as st
import plotly.express as px
from dataset import *
from graficos import *


st.set_page_config(layout='wide')
st.title('Dashboard de Vendas :shopping_trolley:')

aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
with aba1:
    st.dataframe(df)
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
    st.plotly_chart(receita_vendedor, use_container_width=True)