# Projeto de Regressão Logística

# Projeto com um conjunto de dados indicando se um usuário de internet específico clicou ou não em uma propaganda
# Criação de um modelo que preveja se um usuário clicará ou não em um anúncio baseado nos recursos desse usuário

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')


print('\n\n# Leitura do dataset')
dfData = pd.read_csv('machine-learning/df/advertising.csv')


print('\n\n# Visualizando informações importantes da dataset')
print(dfData.head())
print(dfData.info())
print(dfData.describe())







# ## Análise de dados exploratória
# 
# Vamos usar Seaborn para explorar os dados!
# 
# Tente recriar os gráficos abaixo.
# 
# ** Crie um histograma de "Age" **





# ** Crie um joinplot mostrando "Area Income" versus "Age" **





# ** Crie um jointplot que mostre as distribuições KDE do "Daily Time spent" no site vs "Age". **





# ** Crie um jointplot do 'Daily Time Spent on Site' vs. 'Daily Internet Usage'**





# ** Finalmente, crie um parplot com o matiz definido pelo recurso de coluna 'Clicked on Ad'. **





# 
# # Regressão Logística
# 
# Agora é hora de quebrar nossos dados em treino e teste e fitar nosso modelo.
# 
# Você terá a liberdade aqui para escolher colunas em que deseja treinar!

# ** Divida os dados em conjunto de treinamento e conjunto de testes usando train_test_split **













# ** Treine e ajuste um modelo de regressão logística no conjunto de treinamento. **









# ## Previsões e avaliações
# ** Agora preveja valores para os dados de teste. **





# ** Crie um relatório de classificação para o modelo. **





# * 'Daily Time Spent on Site': tempo no site em minutos.
# * 'Age': idade do consumidor.
# * 'Area Income': Média da renda do consumidor na região.
# * 'Daily Internet Usage': Média em minutos por di que o consumidor está na internet.
# * 'Linha do tópico do anúncio': Título do anúncio.
# * 'City': Cidade do consumidor.
# * 'Male': Se o consumidor era ou não masculino.
# * 'Country': País do consumidor.
# * 'Timestamp': hora em que o consumidor clicou no anúncio ou janela fechada.
# * 'Clicked on Ad'': 0 ou 1 indicam se clicou ou não no anúncio.




