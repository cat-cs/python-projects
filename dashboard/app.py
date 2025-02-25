import streamlit as st
import plotly.express as px
from dataset import df

st.set_page_config(layout='wide')
st.title('Dashboard de Vendas :shopping_trolley:')

aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
with aba1:
    st.dataframe(df)
with aba2: 
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', df['Preço'].sum())
    with coluna2: 
        st.metric("Quantidade de Vendas", df.shape[0])