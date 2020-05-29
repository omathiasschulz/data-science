# Projeto de análise de dados do mercado financeiro

# Foco do projeto: Ações dos banco e como eles performaram durante a crise financeira até o início de 2016
# Crise financeira: https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308


import pandas as pd
import numpy as np


print('\n\n# Leitura do CSV')
DIRECTORY = 'projetos/df/'
FILENAME = 'mercado-financeiro.csv'
newDF = pd.read_csv(DIRECTORY + FILENAME, header=[0, 1], index_col=0)
print(newDF.head())
print(newDF.info())





# # Análise de dados exploratória
# 
# Vamos explorar os dados um pouco! Antes de prosseguir, sugiro que você verifique a documentação no [Multi-Level Indexing](http://pandas.pydata.org/pandas-docs/stable/advanced.html) e [como usar .xs](http: // pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html).
# Consulte as soluções se você não consiga descobrir como usar .xs (), uma vez que isso será uma parte importante desse projeto.
# 
# ** Qual é o preço máximo de fechamento para cada banco durante todo o período? **


# ** Crie um novo DataFrame vazio chamado returns. Este dataframe conterá os retornos para o ação de cada banco. Os retornos geralmente são definidos por: **
# 
# $$r_t = \frac{p_t - p_{t-1}}{p_{t-1}} = \frac{p_t}{p_{t-1}} - 1$$


# ** Podemos usar o método pct_change () pandas na coluna close para criar uma coluna que represente esse valor de retorno. Crie um loop for que vá e para cada Bank Stock Ticker cria essa coluna de retorno e configura-a como uma coluna nos dados DataFrame. **



# ** Crie um parplot utilizando seaborn no dataframe de retorno. **



# ** Usando o seu DataFrame returns, descubra quais datas cada ação dos bancos teve o melhor e o pior dia de retorno. Você deve notar que 4 dos bancos compartilham o mesmo dia para a pior queda. Alguma coisa significante aconteceu naquele dia? **

# ** Dê uma olhada no desvio padrão dos retornos. Qual ação você classificaria como a mais arriscada durante todo o período de tempo? Qual você classificaria como a mais arriscado para o ano 2015? **


# ** Crie um distplot usando seaborn dos retornos de 2015 para Morgan Stanley **


# ** Crie um distplot usando seaborn dos retornos de 2008 para CitiGroup **


# # Mais visualização
# 
# Muito desse projeto se concentrará em visualizações. Sinta-se livre para usar qualquer uma das suas bibliotecas de visualização preferidas para tentar recriar os plots descritos abaixo, seaborn, matplotlib, plotly e cufflinks, ou apenas pandas.
# 
# ### Importações


# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style('whitegrid')
# get_ipython().run_line_magic('matplotlib', 'inline')


# ** Crie um gráfico de linha mostrando o preço de fechamento para cada banco para todo o índice de tempo. (Sugestão: tente usar um loop for ou use [.xs](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html) para obter uma seção transversal dos dados .) **



# ## Médias móveis
# 
# Vamos analisar as médias móveis para essas ações no ano de 2008.
# 
# ** Trace a média de 30 dias para o preço do Bank Of America para o ano de 2008 **


# ** Crie um mapa de calor da correlação entre os preços de fechamento das ações. **


# ** Opcional: use o clustermap do seaborn para agrupar as correlações: **


# Definitivamente, muitos tópicos de finanças específicos aqui, então não se preocupe se você não os entendeu todos! A única coisa que você deve estar preocupado com a compreensão são os pandas básicos e operações de visualização.
