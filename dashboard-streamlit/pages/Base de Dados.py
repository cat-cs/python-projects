import streamlit as st
from dataset import df
from utils import converte_csv, converte_json


st.set_page_config(layout='wide', page_title = 'Base de Dados')
st.title('Dataset de Vendas')

with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as colunas', 
        list(df.columns),
        list(df.columns)
    )

st.sidebar.title('Filtros')
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect(
        'Selecione a categoria', 
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
    )
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider(
        'Selecione o preço', 
        0, 5000, (0, 5000)
    )

with st.sidebar.expander('Data de Compra'):
    data_compra = st.date_input(
        'Selecione a data',
        (df['Data da Compra'].min(),
        df['Data da Compra'].max())
    )

query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''
dados_filtrados = df.query(query)
dados_filtrados = dados_filtrados[colunas]
st.dataframe(dados_filtrados)

st.markdown(f'Exibindo {dados_filtrados.shape[0]} linhas e {dados_filtrados.shape[1]} colunas')


coluna1, coluna2 = st.columns(2)
with coluna1:
    st.download_button(
        'Importar arquivo em CSV',
        data= converte_csv(dados_filtrados),
        file_name='vendas.csv',
        on_click= lambda: st.success (f'Arquivo CSV gerado com sucesso!'),
        mime='text/csv')
with coluna2:
    st.download_button(
        'Importar arquivo em JSON',
        data= converte_json(dados_filtrados),
        file_name='vendas.json',
        on_click= lambda: st.success (f'Arquivo JSON gerado com sucesso!'),
        mime='application/json')
