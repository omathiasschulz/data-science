# Ligações para o 911


# Projeto de análise de alguns dados de chamadas para o 911
# Dataset disponível no Kaggle
# https://www.kaggle.com/mchirico/montcoalert


# Colunas do dataset:
# * lat: Variável String, Latitude
# * lng: Variável String, Longitude
# * desc: Variável String, Descrição da Chamada de Emergência
# * zip: Variável String, CEP
# * título: Variável String, Título
# * timeStamp: Variável String, AAAA-MM-DD HH: MM: SS
# * twp: Variável String, Township
# * addr: Variável String, Endereço
# * e: Variável String, variável Dummy (sempre 1)


# Importações necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')


print ('\n\n# Lendo o arquivo csv e visualizando suas informações')
df = pd.read_csv('projetos/df/911.csv')
print(df.info())
print(df.head())


print('\n\n# Top 5 CEPs nas chamadas 911 (Que mais se repetem)')
print(df['zip'].value_counts().head(5))


print('\n\n# Os 5 principais municípios nas chamadas 911')
print(df['twp'].value_counts().head(5))


print('\n\n# Coluna "title". Quantidade de códigos de título exclusivos')
print(df['title'].value_counts().count())
# OU
# print(df['title'].nunique())
# print(len(df['title'].unique()))


print('\n\n# Criação da coluna reason a partir da coluna title')
# Por exemplo:
# Coluna title EMS: BACK PAINS / BLESSOR
# Razão: EMS
df['reason'] = df.apply(lambda column : column['title'].split(':')[0], axis=1)
# OU
# df['reason'] = df['title'].apply(lambda title: title.split(':')[0])
print(df.head())
print(df['reason'].value_counts())


print('\n\n# Motivo mais comum para uma chamada do 911 com base na reason')
print(df['reason'].value_counts())
print(df['reason'].value_counts().head(1))


print('\n\n# Seaborn - Countplot de chamadas 911 baseadas na coluna reason')
sns.countplot(x='reason', color='blue', data=df)
plt.show()


print('\n\n# Tipo de dados dos objetos na coluna timeStamp')
print(df['timeStamp'].dtypes)


print('\n\n# Converter a coluna timeStamp em objetos DateTime')
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
print(df['timeStamp'].dtypes)


print('\n\n# Pegando a hora da coluna timeStamp')
time = df['timeStamp'].iloc[0]
print(time.hour)


print('\n\n# Criação das novas colunas hour, month e dayWeek')
df['hour'] = df['timeStamp'].dt.hour
df['month'] = df['timeStamp'].dt.month
df['dayWeek'] = df['timeStamp'].dt.dayofweek


print('\n\n# Conversão do dia da semana número para texto')
days = {
    0: 'Segunda', 
    1: 'Terça', 
    2: 'Quarta', 
    3: 'Quinta', 
    4: 'Sexta', 
    5: 'Sábado', 
    6: 'Domingo',
}
df['dayWeekText'] = df['dayWeek'].apply(lambda column : days[column])
# OU
# df['Day of Week'] = df['Day of Week'].map(dmap)


print('\n\n# Seaborn - Countplot da coluna dayWeek com a tonalidade baseada na coluna reason')
sns.countplot(x='dayWeek', data=df, hue='reason', palette='viridis')
plt.legend(loc=1)
plt.show()


print('\n\n# Seaborn - Countplot da coluna month com a tonalidade baseada na coluna reason')
sns.countplot(x='month', data=df, hue='reason', palette='viridis')
plt.legend(loc=1)
plt.show()


print('\n\n# Preenchendo os meses que faltam')

# Count das colunas por mês
byMonth = df.groupby('month').count()
print(byMonth.head(12))





# ** Agora crie um plot simples fora do Dataframe indicando a contagem de chamadas por mês. **


# ** Agora veja se você pode usar o lmplot () do Seaborn para criar um modelo linear no número de chamadas por mês. 
# Tenha em mente que talvez seja necessário resetar o índice em uma coluna. **


# ** Crie uma nova coluna chamada 'Data' que contenha a data da coluna timeStamp. 
# Você precisará usar .apply() junto com o método .date(). **


# ** Agora agrupe esta coluna Data com o groupby. Usando o count (), crie um gráfico de contagens de chamadas 911. **


# ** Agora recrie esse plot, mas crie 3 plots separados com cada plot representando uma Razão para a chamada 911 **






# ** Agora vamos continuar a criar mapas de calor com seaborn e nossos dados. 
# Em primeiro lugar, devemos reestruturar o quadro de dados para que as colunas se tornem 
# horas e o Índice se torne o Dia da Semana. Há muitas maneiras de fazer isso,
# mas eu recomendaria tentar combinar groupby com o método [unstack]
# (http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.unstack.html) . 
# Consulte as soluções se você ficar preso nisso! **


# ** Agora crie um mapa de calor usando este DataFrame **


# ** Agora crie um clustermap usando este DataFrame. **


# ** Agora repita estes mesmos plots e operações para um DataFrame que mostra o mês como a coluna. **






