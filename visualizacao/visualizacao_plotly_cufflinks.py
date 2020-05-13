import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from plotly import __version__

# Visualizar a versão do plotly
print(__version__)

# Importar as bibliotecas e utilizar offline
from plotly.offline import download_plotlyjs, plot, iplot
import cufflinks as cf
cf.go_offline()


# Dataframes fictícios
df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
print(df.head())
df2 = pd.DataFrame({'Categoria':['A', 'B', 'C'], 'Valores':[32, 43, 50]})
print(df2.head())
df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})
print(df3.head())


# Visualização normal a partir de métodos embutidos no pandas (Gráfico de dispersão)
# Gráfico de dispersão = Onde X e Y se encontram é marcado um ponto
df.plot(kind='scatter', x='A', y='B')
plt.show()

# Visualização a partir do Plotly (Gráfido de linha)
fig = df.iplot(asFigure=True, kind='scatter', x='A', y='B')
fig.show()

# Visualização a partir do Plotly (Gráfido de dispersão)
fig = df.iplot(asFigure=True, kind='scatter', x='A', y='B', mode='markers')
fig.show()

# Visualização a partir do Plotly (Gráfido de barra)
fig = df2.iplot(asFigure=True, kind='bar', x='Categoria', y='Valores')
fig.show()

# Visualização a partir do Plotly (Gráfido de barra)
# Contar quantas vezes possuem elementos nas quatro colunas
fig = df.count().iplot(asFigure=True, kind='bar')
fig.show()

# Visualização a partir do Plotly (Gráfido de caixa)
fig = df.iplot(asFigure=True, kind='box')
fig.show()

# Visualização a partir do Plotly (Gráfido 3D)
fig = df3.iplot(asFigure=True, kind='surface', colorscale='rdylbu')
fig.show()

# Visualização a partir do Plotly (Gráfico de diferença)
# Monitar o desempenho de duas variáveis
fig = df[['A', 'B']].iplot(asFigure=True, kind='spread')
fig.show()

# Visualização a partir do Plotly (Gráfico de histograma)
fig = df[['A']].iplot(asFigure=True, kind='hist', bins=50)
fig.show()

# Visualização a partir do Plotly (Gráfico de bolha)
# Gráfico de bolha = É um gráfico de dispersão onde o tamanho das bolhas são
# determinados em função de uma terceira variável 
fig = df.iplot(asFigure=True, kind='bubble', x='A', y='B', size='C')
fig.show()
