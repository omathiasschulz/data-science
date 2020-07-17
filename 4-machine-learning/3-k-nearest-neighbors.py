# K Nearest Neighbors - Projeto 

# Projeto de KNN com um conjunto de dados customizados


import pandas as pd
import numpy as np
import seaborn as sns
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


print('\n\n# Realizando a leitura do dataset')
df = pd.read_csv('machine-learning/df/KNN_Project_Data')


print('\n\n# Visualizando algumas informações do dataset')
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)


print('\n\n# Análise exploratória de dados - Pairplot com a tonalidade indicada pela coluna TARGET CLASS')
sns.pairplot(df, hue='TARGET CLASS', palette='coolwarm')
plt.savefig('machine-learning/graficos/3-k-nearest-neighbors-pairplot')
plt.close()


print('\n\n# Padronizado as variáveis')
scaler = StandardScaler()

print('Dropando a coluna TARGET CLASS')
dfX = df.drop('TARGET CLASS', axis=1)
print(dfX.head(5))

print('Treinando o modelo')
scaler.fit(dfX)

print('Transformando os parâmetros em uma versão padronizada')
scaled = scaler.transform(dfX)
print(scaled)

print('\n\nConvertendo para um dataframe e visualizando se a transformação funcionou')
dfPadronizado = pd.DataFrame(scaled, columns=df.columns[:-1])
print(dfPadronizado.head(10))


print('\n\n# Dividindo o dataset em treino e teste')
X = dfPadronizado
Y = df['TARGET CLASS']
xTreino, xTeste, yTreino, yTeste = train_test_split(X, Y, test_size=0.3)


print('\n\n# Utilizando o KNN')
model = KNeighborsClassifier(n_neighbors=1)
model.fit(xTreino, yTreino)


print('\n\n# Previsões e avaliações do modelo KNN')
predict = model.predict(xTeste)


print('\n\n# Criando uma matriz de confusão')
print(confusion_matrix(yTeste, predict))


print('\n\n# Criando um relatório de classificação')
print(classification_report(yTeste, predict))


print('\n\n# Buscando um possível melhor valor para K e com isso uma melhor previsão e avaliação')
errorRate = []
for i in range(1, 50):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(xTreino, yTreino)
    predict = model.predict(xTeste)
    errorRate.append(np.mean(predict != yTeste))


print('\n\n# Gráfico com as informações de erro em cada valor para K')
plt.figure(figsize=(14,8))
plt.plot(range(1, 50), errorRate, color='green', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K Value')
plt.ylabel('Error Rate')
plt.show()


print('\n\n# Treinando novamente o modelo com o melhor valor de K e refazendo a matriz de confução e o relatório de classficação')
model = KNeighborsClassifier(n_neighbors=36)
model.fit(xTreino, yTreino)
predict = model.predict(xTeste)
errorRate.append(np.mean(predict != yTeste))
print(confusion_matrix(yTeste, predict))
print(classification_report(yTeste, predict))
