import json
import pandas as pd


file = open('dashboard-streamlit/vendas.json')
data = json.load(file)
file.close()

df = pd.DataFrame.from_dict(data)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format= '%d/%m/%Y')
df['Categoria do Produto'] = df['Categoria do Produto'].str.title()
df['Tipo de pagamento'] = df['Tipo de pagamento'].str.split('_').str.join(' ').str.title()

df_total = df.drop(columns=['lat', 'lon'])
df_total['Data da Compra'] = df_total['Data da Compra'].dt.date
df_total['Frete'] = df_total['Frete'].map('{:.2f}'.format)

df_estado = df.groupby('Local da compra')[['Preço']].sum()
df_estado = df.drop_duplicates(subset= 'Local da compra')[['Local da compra','lat', 'lon']].merge(df_estado, left_on='Local da compra', right_index=True)
df_estado.sort_values(by='Preço', ascending=False)

df_receita_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))[['Preço']].sum().reset_index()
df_receita_mensal['Ano'] = df_receita_mensal['Data da Compra'].dt.year
df_receita_mensal['Mês'] = df_receita_mensal['Data da Compra'].dt.month_name()

df_receita_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values(by='Preço', ascending=False)

df_vendedor = df.groupby('Vendedor')['Preço'].agg(['sum', 'count'])

