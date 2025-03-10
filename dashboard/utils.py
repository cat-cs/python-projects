import streamlit as st
import pandas as pd


def formatar_numero(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor < 1000:
            return f'{prefixo}{valor:.2f}{unidade}'
        valor /= 1000
    return f'{prefixo}{valor:.2f} milhões'

@st.cache_data
def converte_csv(df):
    return df.to_csv(index=False).encode('utf-8')
     
def converte_json(df):
    return df.to_json(orient='records').encode('utf-8')

