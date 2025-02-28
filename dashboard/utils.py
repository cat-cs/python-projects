import streamlit as st

def formatar_numero(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor < 1000:
            return f'{prefixo}{valor:.2f}{unidade}'
        valor /= 1000
    return f'{prefixo}{valor:.2f} milhões'

@st.cache_data
def converte_csv(df):
    return df.to_csv('vendas.csv', index=False)

def converte_excel(df):
    return df.to_excel('vendas.xlsx', index=False)
     
def converte_json(df):
    return df.to_json('vendas.json', orient='records')
    
def baixar_tabela(tipo_arquivo, df):
    formato_arquivo = {
    'csv': converte_csv,
    'excel': converte_excel,
    'json': converte_json}
    
    st.download_button(
        f'Importar arquivo em {tipo_arquivo}',
        data= formato_arquivo[tipo_arquivo](df),
        file_name=f'vendas.{tipo_arquivo}',
        on_click= st.success (f'Arquivo {tipo_arquivo} gerado com sucesso!'),
        mime='text/{tipo_arquivo}')
    