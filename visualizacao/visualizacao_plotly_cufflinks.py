import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importar as bibliotecas e utilizar offline
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
cf.go_offline()

# Plotly Express
# Interface de alto nível fácil de usar do Plotly que produz figuras
import plotly.express as px

# Permite visualizar cada ponto, salvar como png, salvar na nuvem, 
# realizar um zoom, se mover no gráfico

# Dataframe fictício
df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
print(df.head())

df2 = pd.DataFrame({'Categoria':['A', 'B', 'C'], 'Valores':[32, 43, 50]})
print(df2.head())


# # Gráfico de dispersão utilizando o dataset Iris
# df_iris = px.data.iris()
# fig = px.scatter(
#     df_iris, x='sepal_length', y='sepal_width', color='species', size='petal_length'
# )
# fig.show()

# # Gráfico de dispersão
# fig = px.scatter(df, x='A', y='B')
# fig.show()

# # Gráfico de barra
# fig = px.bar(df2, x='Categoria', y='Valores')
# fig.show()

df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})
df3.iplot(kind='surface',colorscale='rdylbu')
fig = px.s(df2, x='Categoria', y='Valores')
fig.show()



# df.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)

# df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})
# df3.iplot(kind='surface',colorscale='rdylbu')