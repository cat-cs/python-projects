import json
import pandas as pd

file = open('dashboard/vendas.json')
data = json.load(file)
file.close()

df = pd.DataFrame.from_dict(data)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format= '%d/%m/%Y')


def formatar_numero(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor < 1000:
            return f'{prefixo}{valor:.2f}{unidade}'
        valor /= 1000
    return f'{prefixo}{valor:.2f} milhões'

df_estado = df.groupby('Local da compra')[['Preço']].sum()
df_estado = df.drop_duplicates(subset= 'Local da compra')[['Local da compra','lat', 'lon']].merge(df_estado, left_on='Local da compra', right_index=True)
df_estado.sort_values(by='Preço', ascending=False)

df_receita_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))[['Preço']].sum().reset_index()
df_receita_mensal['Ano'] = df_receita_mensal['Data da Compra'].dt.year
df_receita_mensal['Mês'] = df_receita_mensal['Data da Compra'].dt.month_name()

df_receita_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values(by='Preço', ascending=False)

df_receita_vendedor = df.groupby('Vendedor')[['Preço']].agg(['sum', 'count'])