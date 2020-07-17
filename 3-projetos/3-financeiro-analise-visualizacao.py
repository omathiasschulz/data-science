# Projeto de análise de dados do mercado financeiro

# Foco do projeto: Ações dos banco e como eles performaram durante a crise financeira até o início de 2016
# Crise financeira: https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print('\n\n# Leitura do CSV')
DIRECTORY = 'projetos/df/'
FILENAME = 'mercado-financeiro.csv'
dfBanks = pd.read_csv(DIRECTORY + FILENAME, header=[0, 1], index_col=0)
print(dfBanks.head())
print(dfBanks.info())


print('\n\n# Análise de dados exploratória')

print('\n\n## Preço máximo de fechamento para cada banco durante todo o período')

print('### De apenas um banco: ')
print(dfBanks.xs(('BAC', 'Close'), axis=1).max())

print('### Todos os bancos: ')
print(dfBanks.xs(key='Close', axis=1, level='Stock Info').max())


print('\n\n# Novo DataFrame vazio chamado returns')
returns = pd.DataFrame()


print('\n\n# DataFrame com os retornos para o ação de cada banco')
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
for tick in tickers:
    returns[tick + 'Return'] = dfBanks[tick]['Close'].pct_change()
print(returns.head())


print('\n\n# Parplot utilizando seaborn no dataframe de retorno')
sns.pairplot(returns)
plt.show()


print('\n\n# Datas de cada ação dos bancos que teve o melhor e o pior dia de retorno')
print(returns.idxmin())
print(returns.idxmax())


print('\n\n# Desvio padrão dos retornos')
print(returns.std())


print('\n\n# Desvio padrão dos retornos apenas no ano de 2015')
print(returns.loc['2015-01-01':'2015-12-31'].std())


print('\n\n# Distplot usando seaborn dos retornos de 2015 para Morgan Stanley')
sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MSReturn'])
plt.show()


print('\n\n# Distplot usando seaborn dos retornos de 2008 para CitiGroup')
sns.distplot(returns.loc['2008-01-01':'2008-12-31']['CReturn'])
plt.show()


print('\n\n# Gráfico de linha mostrando o preço de fechamento para cada banco para todo o índice de tempo')

print('\n## Forma 01:')
for tick in tickers:
    dfBanks[tick]['Close'].plot(figsize=(12, 4), label=tick)
plt.legend()
plt.show()

print('\n## Forma 02:')
dfBanks.xs(key='Close',axis=1,level='Stock Info').plot(figsize=(12, 4))
plt.show()


print('\n\n# Médias móveis (média de 30 dias) para o preço do Bank Of America para o ano de 2008')
dfBAC = dfBanks['BAC']
plt.figure(figsize=(12,6))
dfBAC['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='Média móvel de 30 dias')
dfBAC['Close'].loc['2008-01-01':'2009-01-01'].plot(label='Fechamento Bank Of America')
plt.legend()
plt.show()


print('\n\n# Mapa de calor da correlação entre os preços de fechamento das ações')
matrixCorrelacao = dfBanks.xs(key='Close',axis=1,level='Stock Info').corr()
sns.heatmap(matrixCorrelacao, annot=True)
plt.show()
