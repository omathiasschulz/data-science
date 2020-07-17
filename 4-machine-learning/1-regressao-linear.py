# Regressão Linear - Projeto

# Empresa de comércio eletrônico que vende roupas online e possui sessões de consultoria em estilo e vestuário na loja
# Os clientes entram na loja, têm reuniões com um estilista pessoal e 
# podem ir para casa e encomendarem em um aplicativo móvel ou site para a roupa que desejam.
# 
# Projeto de analise dos dados dos clientes para a empresa decidir se deve concentrar 
# seus esforços em sua experiência em aplicativos móveis ou em seu site


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


print('\n\n# Leitura do dataset')
dfClientes = pd.read_csv('machine-learning/df/EcommerceCustomers')


print('\n\n# Visualizando as informações do dataset')
print(dfClientes.head())
print(dfClientes.info())
print(dfClientes.describe())



print('\n\n\n### Análise de dados exploratória')

print('\n\n# Jointplot comparando as colunas Time on Website (Tempo no site) e Yearly Amount Spent (Total gasto anual)')
sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=dfClientes)
plt.show()


print('\n\n# Jointplot comparando as colunas Time on App (Tempo no app) e Yearly Amount Spent (Total gasto anual)')
sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=dfClientes)
plt.show()


print('\n\n# Jointplot hexagonal 2D comparando as colunas Time on App (Tempo no app) e Length of Membership (Tempo da Associação)')
sns.jointplot(x='Time on App', y='Length of Membership', data=dfClientes, kind='hex')
plt.show()


print('\n\n# Gráfico pairplot do dataset')
sns.pairplot(data=dfClientes)
plt.savefig('machine-learning/graficos/1-regressao-linear-pairplot')
plt.show()

print('\n# Baseado no gráfico pairplot:')
print('Característica mais correlacionada com o Yearly Amount Spent é o Length of Membership')

print('\n# Gráfico do modelo linear das colunas Yearly Amount Spent e Length of Membership')
sns.lmplot(x='Yearly Amount Spent', y='Length of Membership', data=dfClientes)
plt.show()



print('\n\n\n### Treinando e teste com os dados')


print('\n\n# Separando o dataset')
print('X = características numéricas dos clientes')
print('y = Valor anual gasto (Yearly Amount Spent')
print(dfClientes.columns)
X = dfClientes[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
Y = dfClientes[['Yearly Amount Spent']]


print('\n\n# Dividindo os dados em conjuntos de treinamento e teste')
xTreino, xTeste, yTreino, yTeste = train_test_split(X, Y, test_size=0.3)


print('\n\n# Treinando o modelo')
lm = LinearRegression()
lm.fit(xTreino, yTreino)


print('\n\n# Coeficientes do modelo')
print(lm.coef_)


print('\n\n# Avaliando o desempenho do modelo ao prever os valores de teste!')
yTesteResult = lm.predict(xTeste)


print('\n\n# Diagrama de dispersão (scatterplot) dos valores reais de teste em relação aos valores preditos')
plt.scatter(yTeste, yTesteResult)
plt.xlabel('Y Teste')
plt.ylabel('Y Predição')
plt.show()



print('\n\n\n### Avaliando o Modelo')


print('\n\n# Erro absoluto médio, Erro quadrado médio, Erro quadrado médio da raiz')
print('MAE:', metrics.mean_absolute_error(yTeste, yTesteResult))
print('MSE:', metrics.mean_squared_error(yTeste, yTesteResult))
print('RMSE:', np.sqrt(metrics.mean_squared_error(yTeste, yTesteResult)))



print('\n\n\n### Resíduos')


print('\n\n# Traçando um histograma dos resíduos e verificando se parece normalmente distribuído')
sns.distplot((yTeste, yTesteResult), bins=50)
plt.show()



print('\n\n\n### Conclusão')


print('\n\n# Interpretando os coeficientes')
coeficientes = pd.DataFrame(lm.coef_[0], X.columns, columns=['Coeficientes'])
print(coeficientes)

print('O aumento de 1 unidade na média de tempo de uso está associado a um aumento de 25,98 dólares totais gastos.')
print('O aumento de 1 unidade no tempo gasto no App está associado a um aumento de 38,59 dólares totais gastos.')
print('O aumento de 1 unidade no tempo no site está associado a um aumento de 0,19 dólares em dólares.')
print('O aumento de 1 unidade no tempo de Associação está associado a um aumento de 61,27 dólares em dólares.')


print('\n\n# A empresa deve se concentrar mais em seu aplicativo móvel ou em seu site?')

print('Deve investir mais no aplicativo móvel, dado que o mesmo apresenta um coeficiente significativamente maior do que o site')
print('Entretanto, a empresa deveria arranjar outras formas de fidelizar seu cliente, visto que essa é a variável que mais influencia os gastos dos seus usuários')

