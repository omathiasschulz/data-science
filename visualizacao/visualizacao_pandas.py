import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Alterar o estilo dos gráficos do pandas a partir do Seaborn
import seaborn as sns
plt.style.use('ggplot')
# plt.style.use('bmh')
# plt.style.use('dark_background')

# Executar na pasta python
# clear && python visualizacao/visualizacao_pandas.py
print('Visualização de dados embutida ao Pandas')

df1 = pd.read_csv('visualizacao/df/pandas_df1.csv', index_col=0)
print('DF1')
print(df1.head())
df1.info()

df2 = pd.read_csv('visualizacao/df/pandas_df2.csv')
print('DF2')
print(df2.head())
df2.info()

print('Histograma de uma coluna do DF1')
df1['A'].hist()
plt.show()

print('Plot de área')
# df2.plot.area()
df2.plot.area(alpha=0.4)
plt.show()

print('Plot de barra')
# df2.plot.bar()
df2.plot.bar(stacked=True)
plt.show()

print('Histograma de uma coluna do DF1')
df1['A'].plot.hist(bins=50)
plt.show()

print('Scatter Plot')
df1.plot.scatter(x='A', y='B')
plt.show()

print('Scatter Plot')
# c = Define a cor a partir de outra coluna / variável
df1.plot.scatter(x='A', y='B', c='C')
plt.show()

print('Scatter Plot')
# cmap = Alterar a cor
df1.plot.scatter(x='A', y='B', c='C', cmap='inferno')
plt.show()

print('Scatter Plot')
# s = Define o tamanho a partir de outra coluna / variável
df1.plot.scatter(x='A', y='B', s=df1['C']*20)
plt.show()

print('Box Plot')
df2.plot.box()
plt.show()

print('Box Plot')
# Criar um dataframe
df = pd.DataFrame(np.random.rand(1000, 2), columns=['A', 'B'])
print(df.head())

print('Criar um mapa de calor com hexagonos')
df.plot.hexbin(x='A', y='B', gridsize=20, cmap='Oranges')
plt.show()

print('Plot de KDE')
df2.plot.kde()
plt.show()


# Utilizando o DF3
df3 = pd.read_csv('visualizacao/df/pandas_df3.csv')
print(df3.head())
df3.info()

print('Gráfico de Dispersão das colunas A e B do DF3')
df3.plot.scatter(x='a', y='b', color='red', s=50, figsize=(12, 3))
plt.show()

print('Histograma da coluna A')
df3['a'].plot.hist()
plt.show()

print('Histograma da coluna A com mais colunas')
df3['a'].plot.hist(alpha=0.5, bins=25)
plt.show()

print('Boxplot de comparação entre as colunas A e B')
df3[['a', 'b']].plot.box()
plt.show()

print('Plot de KDE da coluna D')
df3['d'].plot.kde()
plt.show()

print('Plot de KDE da coluna D (modificada)')
df3['d'].plot.kde(lw=5, ls=':')
plt.show()

print('Plot de Área das 30 primeiras linhas')
df3[:30].plot.area(alpha=0.4, cmap='icefire')
plt.show()

print('Plot de Área das 30 primeiras linhas')
df3[:30].plot.area(alpha=0.4, cmap='icefire', figsize=(8, 7))
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
