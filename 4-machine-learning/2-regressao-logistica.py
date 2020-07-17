# Projeto de Regressão Logística

# Projeto com um conjunto de dados indicando se um usuário de internet específico clicou ou não em uma propaganda
# Criação de um modelo que preveja se um usuário clicará ou não em um anúncio baseado nos recursos desse usuário

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


print('\n\n# Leitura do dataset')
dfData = pd.read_csv('machine-learning/df/advertising.csv')


print('\n\n# Visualizando informações importantes da dataset')
print(dfData.head())
print(dfData.info())
print(dfData.describe())



print('\n\n\n### Análise de dados exploratória')

print('\n\n# Histograma da coluna  "Age"')
dfData['Age'].hist(bins=30)
plt.xlabel('Age')
plt.show()


print('\n\n# Joinplot mostrando Area Income (Média da renda do consumidor na região) versus Age (Idade do consumidor)')
sns.jointplot(x='Area Income', y='Age', data=dfData)
plt.show()


print('\n\n# Jointplot mostrando as distribuições KDE do Daily Time Spent on Site (tempo no site em minutos) versus Age (idade do consumidor)')
sns.jointplot(x='Daily Time Spent on Site', y='Age', data=dfData, kind='kde')
plt.show()


print('\n\n# Jointplot mostrando Daily Time Spent on Site (tempo no site em minutos) versus Daily Internet Usage (Média em minutos por dia na internet)')
sns.jointplot(x='Daily Time Spent on Site', y='Daily Internet Usage', data=dfData)
plt.show()


print('\n\n# Pairplot definido pelo recurso de coluna Clicked on Ad')
sns.pairplot(dfData, hue='Clicked on Ad', palette='bwr')
plt.show()



print('\n\n\n### Regressão Logística')

print('\n\n# Separando o dataset em treino e teste')
X = dfData[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']]
Y = dfData[['Clicked on Ad']]

xTreino, xTeste, yTreino, yTeste = train_test_split(X, Y, test_size=0.3)


print('\n\n# Treinando e ajustando o modelo de regressão logística no conjunto de treinamento')
model = LogisticRegression()
model.fit(xTreino, yTreino)


print('\n\n# Previsões')
predict = model.predict(xTeste)


print('\n\n# Relatório de classificação do modelo')

print(classification_report(yTeste, predict))

