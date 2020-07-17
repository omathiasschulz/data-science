# Pandas

import pandas as pd
import numpy as np

from numpy.random import randn
np.random.seed(101)

# Criar uma planilha
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)

# Nova coluna
df['new'] = df['W'] + df['Y']

# Deletar coluna Forma 01:
# df = df.drop('new', axis=1)
# Deletar coluna Forma 02 (melhor):
df.drop('new',axis=1,inplace=True)

# Buscar elementos por nome
df.loc['B','Y']
df.loc[['A','B'],['W','Y']]

# Buscar elementos por indíces (posições numéricas)
df.iloc[2]

# Valores maiores que zero
df[df>0]

# Busca os valores da coluna Y onde os valores da coluna W são maiores que zero
df[df['W']>0]['Y']

# & e |
df[(df['W']>0) & (df['Y'] > 1)]

# Redefinir para o padrão 0,1 ... n índice
df.reset_index(inplace=True)

# Novo index
novoind = 'CA NY WY OR CO'.split()
df['Estados'] = novoind
df.set_index('Estados', inplace=True)



# Dados ausentes

df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})

# Apaga linhas com valores NaN
df.dropna()

# Apaga linhas com dois valores NaN
df.dropna(thresh=2)

# Substituir NaN por 'Conteúdo'
df.fillna(value='Conteúdo')

# Substitui os NaN pela média da coluna A
df['A'].fillna(value=df['A'].mean())



# Group By

# Cria um DataFrame
data = {'Empresa':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Nome':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Venda':[200,120,340,124,243,350]}
df = pd.DataFrame(data)

print(df.groupby("Empresa").mean())
print(df.groupby("Empresa").sum())
print(df.groupby("Empresa").describe())



# Operações

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

# Apresenta os valores da coluna sem repetidos
print(df['col2'].unique())

# Soma todos os elementos da coluna sem contar repetidos
print(df['col2'].nunique())

# Conta a quantidade de repetidos de cada elemento
print(df['col2'].value_counts())

# Aplicar uma função nos elementos de uma coluna
def times2(x):
    return x*2
print(df['col1'].apply(times2))

# Deletar uma coluna
del df['col1']

# Obter as colunas e índices
print(df.columns)
print(df.index)

# Ordenar
df.sort_values(by='col2') #inplace=False por padrão

# Ler um HTML
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df[0])
