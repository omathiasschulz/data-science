# Pandas - Exercícios

# Compras de Ecommerce
# Dados falsos sobre algumas compras feitas pela Amazon

# Importar o pandas
import pandas as pd

# Ler o arquivo como um DataFrame
ecom = pd.read_csv('analise/df/Ecommerce Purchases')

# Verificar o "head" do DataFrame
print(ecom.head())

# Quantidade de linhas e colunas
print(ecom.columns.value_counts().value_counts()[1])
print(ecom.index.value_counts().value_counts()[1])
# Ou print(ecom.info())

# Preço de compra médio
print(ecom['Purchase Price'].mean())

# Preço de compra mais alto e mais baixo
print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())

# Quantidade de pessoas que possuem Inglês 'en' como sua língua de escolha no site
print(ecom[ecom['Language'] == 'en'].count()[0])

# Quantidade de pessoas que possuem o cargo de Advogado
print(ecom[ecom['Job'] == 'Lawyer'].count()[0])

# Quantidade de pessoas que fizeram a compra durante a AM
# Quantidade de pessoas que fizeram a compra durante a PM
print(ecom['AM or PM'].value_counts())
# Ou:
# print(ecom[ecom['AM or PM'] == 'PM'].count()[0])
# print(ecom[ecom['AM or PM'] == 'AM'].count()[0])

# Os 5 títulos de trabalho mais comuns
print(ecom['Job'].value_counts().head(5))

# Preço de compra para a transação de Lot '90 WT'
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

# Email da pessoa com o seguinte número do cartão de crédito: 4926535242672853
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])

# Quantidade de pessoas que possuem American Express como seu fornecedor de cartão de crédito
#  e fizeram uma compra acima de US $ 95
print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95.0)].count()[0])

# Quantidade de pessoas que possuem um cartão de crédito que expira em 2025
print(len(ecom[ecom['CC Exp Date'].str.split('/').str[1] == '25']))
# Ou:
# print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25'))

# Os 5 principais provedores de e-mail / hosts mais populares
print(ecom['Email'].str.split('@').str[1].value_counts().head(5))
# Ou:
# print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))
