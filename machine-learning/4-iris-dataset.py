# Projeto de Support Vector Machines 

# Conjunto de dados de íris: http://en.wikipedia.org/wiki/Iris_flower_data_set
# O conjunto de dados é composto por 50 amostras de cada uma das três espécies de íris (Iris setosa, Iris virginica e Iris versicolor), de modo que 150 amostras totais. 
# Foram medidas quatro características de cada amostra: o comprimento e a largura das sépalas e pétalas, em centimetros.

# Uma iris setosa http://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg
# Uma iris versicolor http://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg
# Uma iris virginica http://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg

import pandas as pd
import seaborn as sns
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

print('\n\n# Obter os dados utilizando o seaborn para obter os dados da íris ')
dfiris = sns.load_dataset('iris')

print(dfiris.head())
print(dfiris.info())
print(dfiris.describe())


print('\n\n# Análise de dados exploratórios')

print('\n\n# Criando um parplot do conjunto de dados. Qual espécie de flor parece ser a mais separável?')
sns.pairplot(dfiris, hue='species', palette='Dark2')
plt.savefig('machine-learning/graficos/4-iris-pairplot')
plt.close()
print('Setona é a mais fácil de separar')

print('\n\n# kde de comprimento sepal versus largura sepal para espécies de flores setosa')
# Busca o df da espécie setosa
dfsetosa = dfiris[dfiris['species'] == 'setosa']
sns.kdeplot(dfsetosa['sepal_width'], dfsetosa['sepal_length'], cmap='plasma')
plt.show()


print('\n\n# Divisao treino-teste')

print('\n\n# Dividindo os dados em um conjunto de treinamento e um conjunto de testes')
X = dfiris.drop('species', inplace=False, axis=1)
Y = dfiris['species']
xTreino, xTeste, yTreino, yTeste = train_test_split(X, Y, test_size=0.33)


print('\n\n# Treino um modelo')

print('\n\n# Treinando um classificador de SVM')
model = SVC()
model.fit(xTreino, yTreino)


print('\n\n# Avaliação do modelo')

print('\n\n# Previsões do modelo e crie uma matriz de confusão e um relatório de classificação')
predict = model.predict(xTeste)
print('Criando uma matriz de confusão')
print(confusion_matrix(yTeste, predict))
print('Criando um relatório de classificação')
print(classification_report(yTeste, predict))


print('\n\n# O modelo obteve ótimos resultados')
print('\n\n# Ajustando os parâmetros para tentar melhorar ainda mais com o Gridsearch')

print('\n\n# Prática do Gridsearch')

print('\n\n# Criando um dicionário chamado e preenchendo alguns parâmetros para C e gama')
params = {'C': [0.1, 1, 10, 100, 1000], 'gamma': [1, 0.1, 0.01, 0.001]}

print('\n\n# Criando um objeto GridSearchCV e ajustando-o aos dados de treinamento')
gridCV = GridSearchCV(SVC(), params, refit=True, verbose=2)
gridCV.fit(xTreino, yTreino)

print('\n\n# Utilizando o modelo de Grid para algumas previsões usando o conjunto de teste')
print('Criando relatórios de classificação e matrizes de confusão para eles. Teve melhora na previsão?')
predictCV = gridCV.predict(xTeste)
print('Criando uma matriz de confusão')
print(confusion_matrix(yTeste, predictCV))
print('Criando um relatório de classificação')
print(classification_report(yTeste, predictCV))
print('O resultado foi praticamente igual')
