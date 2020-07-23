# Projeto de processamento de linguagem natural

# Neste projeto NLP, o objetivo é classificar Avaliações da Yelp em categorias de 1 estrela ou 5 estrelas com base no conteúdo do texto nas revisões. 
# É utilizado o Conjunto de dados de reviews da Yelp da Kaggle https://www.kaggle.com/c/yelp-recsys-2013

import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_extraction.text import  TfidfTransformer
from sklearn.pipeline import Pipeline

print('\n\n# Lendo o arquivo yelp.csv')
df = pd.read_csv('6-nlp/df/yelp.csv')

print('\n\n# Visualizando informações do dataframe')
print(df.head())
print(df.info())
print(df.describe())

print('\n\n# Nova coluna chamada "comprimento do texto", que é o número de caracteres na coluna de texto')
df['textLength'] = df['text'].apply(len)
print(df['textLength'].head())



print('\n\n\n## Análise exploratória de dados')

print('\n\n# Criando um grid de 5 histogramas de comprimento de texto com base nas classificações das estrelas')
g = sns.FacetGrid(data=df, col='stars')
g.map(plt.hist, 'textLength', bins=20)
plt.show()

print('\n\n# Criando um boxplot do comprimento de texto para cada categoria de estrelas')
sns.boxplot(data=df, x='stars',  y='textLength')
plt.show()

print('\n\n# Criando um countplot do número de ocorrências para cada tipo de classificação de estrelas')
sns.countplot(data=df, x='stars')
plt.show()

print('\n\n# Utilizando groupby para obter os valores médios das colunas numéricas')
stars = df.groupby('stars').mean()
print(stars)

print('\n\n# Utilizando o método corr () nesse conjunto de dados agrupado')
starsCorr = stars.corr()
print(starsCorr)

print('\n\n# Criando um heatmap com base na correlação')
sns.heatmap(starsCorr, cmap='coolwarm', annot=True)
plt.show()



print('\n\n\n## Classificação de PNL')

print('\n\n# Buscando dados que foram de 1 estrela ou 5 estrelas, com isso facilitará a classificação')
dfNew = df[(df['stars'] == 1) | (df['stars'] == 5)]
print(dfNew['stars'].value_counts())

print('\n\n# Separando em X e Y. X e y. X será a coluna texto e y será a coluna estrelas')
X = dfNew['text']
Y = dfNew['stars']

print('\n\n# Criando um objeto CountVectorizer')
cv = CountVectorizer()

print('\n\n# Utilizando o método fit_transform no objeto CountVectorizer')
X = cv.fit_transform(X)



print('\n\n\n## Divisão treino-teste')
xTreino, xTeste, yTreino, yTeste = train_test_split(X, Y, test_size=0.3)



print('\n\n\n## Treinando o modelo')

print('\n\n# Criando uma instância do estimador')
nb = MultinomialNB()

print('\n\n# Ajustando o nb usando os dados de treinamento')
nb.fit(xTreino, yTreino)



print('\n\n\n## Previsões e avaliações')
predict = nb.predict(xTeste)

print('\n\n# Criando uma uma matriz de confusão e um relatório de classificação')
print(confusion_matrix(yTeste, predict))
print('\n')
print(classification_report(yTeste, predict))



print('\n\n\n## Usando o processamento de texto. Testando a inclusão do TF-IDF nesse processo usando um pipeline')

print('\n\n# Criando um pipeline com as seguintes etapas: CountVectorizer (), TfidfTransformer (), MultinomialNB ()')
pipeline = Pipeline([
    # bag of words - strings to token integer counts (sem remover stopwords)
    ('bow', CountVectorizer()),
    # integer counts to weighted TF-IDF scores
    ('tfidf', TfidfTransformer()),
    # train on TF-IDF vectors w/ Naive Bayes classifier
    ('classifier', MultinomialNB()),
])

print('\n\n# Utilizando o Pipeline')

print('\n\n# Refazendo a divisão treino-teste')
print('O pipeline já possui todas as suas etapas de pré-processamento, o que significa que é necessário re-dividir os dados originais ')
X = dfNew['text']
Y = dfNew['stars']
xTreino, xTeste, yTreino, yTeste = train_test_split(X, Y, test_size=0.3)

print('\n\n# Ajustando o pipeline aos dados de treinamento')
pipeline.fit(xTreino, yTreino)

print('\n\n# Previsões e Avaliações do pipeline')
predictPipeline = pipeline.predict(xTeste)

print('\n\n# Criando uma uma matriz de confusão e um relatório de classificação')
print(confusion_matrix(yTeste, predictPipeline))
print('\n')
print(classification_report(yTeste, predictPipeline))

print('\n\n# OBS: Parece que o Tf-Idf realmente piorou as coisas!')
