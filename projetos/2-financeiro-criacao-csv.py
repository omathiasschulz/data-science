# Projeto de análise de dados do mercado financeiro - Criando o CSV

# Foco do projeto: Ações dos banco e como eles performaram durante a crise financeira até o início de 2016
# Crise financeira: https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308


from pandas_datareader import data, wb
import pandas as pd
from datetime import date


print('\n\n# Utilizando o datareader de pandas para obter informações sobre ações para os seguintes bancos:')
print('Bank of America; CitiGroup; Goldman Sachs; JPMorgan Chase; Morgan Stanley; Wells Fargo')

print('\n\n## Obtendo os dados de ações de 1 de janeiro de 2006 a 1º de janeiro de 2016 para cada um dos bancos')
DT_INICIO = date(2006, 1, 1)
DT_FIM = date(2016, 1, 1)

print('\n\n## Bank of America')
dfBAC = data.DataReader('BAC', 'yahoo', start=DT_INICIO, end=DT_FIM)
print(dfBAC)

print('\n\n## CitiGroup')
dfC = data.DataReader('C', 'yahoo', start=DT_INICIO, end=DT_FIM)
print(dfBAC)

print('\n\n## Goldman Sachs')
dfGS = data.DataReader('GS', 'yahoo', start=DT_INICIO, end=DT_FIM)
print(dfBAC)

print('\n\n## JPMorgan Chase')
dfJPM = data.DataReader('JPM', 'yahoo', start=DT_INICIO, end=DT_FIM)
print(dfBAC)

print('\n\n## Morgan Stanley')
dfMS = data.DataReader('MS', 'yahoo', start=DT_INICIO, end=DT_FIM)
print(dfBAC)

print('\n\n## Wells Fargo')
dfWFC = data.DataReader('WFC', 'yahoo', start=DT_INICIO, end=DT_FIM)
print(dfBAC)

print('\n\n## Criação da lista dos símbolos dos tickers em ordem alfabética')
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

print('\n\n## Concatenando todos os DataFrames dos bancos em um só')
dfBanks = pd.concat([dfBAC, dfC, dfGS, dfJPM, dfMS, dfWFC], axis=1, keys=tickers)

print('\n\n## Definindo os nomes das colunas (O df possui uma coluna de dois níveis)')
dfBanks.columns.names = ['Bank Ticker','Stock Info']

print('\n\n## Verificando o cabeçalho do DataFrame criado')
print(dfBanks.head())
print(dfBanks.info())


print('\n\n# Salvando como CSV')
DIRECTORY = 'projetos/df/'
FILENAME = 'mercado-financeiro.csv'
dfBanks.to_csv(DIRECTORY + FILENAME)
