# %%


import pandas as pd
import matplotlib.pyplot as plt

# Ler dados

df = pd.read_csv('vendas.csv')

# Métricas
faturamento = df['Vendas'].sum()
ticket_medio = df['Vendas'].mean()

print("Faturamento Total:", faturamento)
print("Ticket Médio:", round(ticket_medio, 2))

# Agrupamento
vendas_produto = df.groupby('Produto')['Vendas'].sum().sort_values(ascending=False)

# Gráfico bonito
plt.figure()
vendas_produto.plot(kind='bar')
plt.title('Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Vendas')
plt.xticks(rotation=0)

# Salvar imagem (IMPORTANTE)
plt.savefig('grafico_vendas.png')
plt.show()
