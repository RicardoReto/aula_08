import pandas as pd

df_clientes = pd.read_csv('data/clientes.csv')
df_vendas = pd.read_csv('data/vendas.csv')
df_vendas_2 = pd.read_csv('data/vendas_2.csv')
df_vendas_3 = pd.read_csv('data/vendas_3.csv')

"""
print(df_clientes.head()) # Imprime apenas as 5 primeiras linhas
print(df_vendas.head())
print(df_vendas_2.head())
print(df_vendas_3.head())
"""

# Equivale ao UNION ALL do SQL e refaz o índice das tabelas, sem repetições
df_concatena = pd.concat([df_vendas, df_vendas_2, df_vendas_3], ignore_index=True)

# Renomeia as colunas
# df = df_concatena.rename(columns={'venda_id': 'VENDA_ID', 'cliente_id': 'CLIENTE_ID'})

# Apresenta quantidade de linhas e colunas
# print(df_concatena.shape)

df_completo = pd.merge(df_clientes, df_concatena, on="cliente_id")
print(df_completo)
print(df_completo.shape)