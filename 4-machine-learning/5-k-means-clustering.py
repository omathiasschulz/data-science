# Projeto de K Means Clustering  

# Dataset com informações sobre universidades em dois grupos: Privadas e Públicas
# OBS: Os rótulos para este conjunto de dados são existentes, mas NÃO são utilizados
# para o algoritmo de agrupamento KMeans, pois esse é um algoritmo de aprendizado não supervisionado
# Ao usar o algoritmo Kmeans em situações reais, não possuirá rótulos
# Nesse caso, os rótulos são utilizados para tentar ter uma idéia do quão bem o algoritmo foi executado


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix

print('\n\n # Obtendo os dados')
df = pd.read_csv('machine-learning/df/College_Data')
print(df.info())
print(df.head())
print(df.describe())

print('\n\n # Setando a primeira coluna como índice')
df.set_index('Unnamed: 0', inplace=True)
print(df.info())
print(df.head())
print(df.describe())
# Ou ler direto o csv com a primeira linha como o index da coluna
# df = pd.read_csv('machine-learning/df/College_Data', index_col=0)


print('\n\n # Análise exploratória de dados')

print('\n\n # scatterplot de Grad.Rate (Taxa de graduação) versus Room.Board (Custos da sala) onde os pontos são coloridos pela coluna "Private"')
sns.scatterplot(data=df, x='Grad.Rate', y='Room.Board', hue='Private', palette='coolwarm')
plt.show()

print('\n\n # scatterplot de  F.Undergrad (Número de alunos de graduação em tempo integral) versus Outstate (Aulas fora do estado) onde os pontos são coloridos pela coluna "Private"')
sns.scatterplot(data=df, x='F.Undergrad', y='Outstate', hue='Private', palette='coolwarm')
plt.show()

print('\n\n # histograma empilhado que mostra o Outstate com base na coluna Private')
sns.set_style('darkgrid')
g = sns.FacetGrid(data=df, hue='Private', size=6, palette='coolwarm', aspect=2)
g = g.map(plt.hist, 'Outstate', bins=20, alpha=0.5)
plt.show()

print('\n\n # histograma empilhado que mostra o Grad.Rate com base na coluna Private')
print('\n\n # ')
sns.set_style('darkgrid')
g = sns.FacetGrid(data=df, hue='Private', size=6, palette='coolwarm', aspect=2)
g = g.map(plt.hist, 'Grad.Rate', bins=20, alpha=0.5)
plt.show()

print('\n\n # Parece haver uma escola particular com uma taxa de graduação superior a 100%. Qual é o nome dessa escola?')
print(df[df['Grad.Rate'] > 100])

print('\n\n # Definindo a taxa de graduação dessa escola para 100')
df['Grad.Rate']['Cazenovia College'] = 100
print(df[df['Grad.Rate'] > 100])


print('\n\n # Criação de clusters K Means')

print('\n\n # Criando uma instância do modelo K Means com 2 clusters')
model = KMeans(n_clusters=2)

print('\n\n # Fitando o modelo para todos os dados, exceto para o rótulo privado')
model.fit(df.drop('Private', inplace=False, axis=1))

print('\n\n # Quais são os vetores centrais do cluster?')
print(model.cluster_centers_)

print('\n\n # Avaliação')
print('Não há uma maneira perfeita de avaliar o agrupamento se você não tiver os rótulos, no entanto, como isso é apenas um exercício, temos os rótulos então aproveitamos isso para avaliar nossos clusters')
print('Entretanto os rótulos não existirão no mundo real')

print('\n\n # Nova coluna para df chamado Cluster, que é 1 para escola particular e 0 para uma escola pública')
def clusterColumn(value):
    if value == 'Yes':
        return 1
    else:
        return 0
df['Cluster'] = df['Private'].apply(clusterColumn)
print(df['Cluster'])

print('\n\n # Criando uma matriz de confusão e um relatório de classificação para ver o quão bem o clustering K Means funcionou sem ter nenhum rótulo')
print('Criando uma matriz de confusão')
print(confusion_matrix(df['Cluster'], model.labels_))
print('Criando um relatório de classificação')
print(classification_report(df['Cluster'], model.labels_))

print('\n\n # Considerando que o algoritmo está usando apenas os recursos para agrupar as universidades em 2 grupos distintos o resultado foi bom')
print('Esse resultado mostras que o K Means é útil para agrupar dados não rotulados!')
