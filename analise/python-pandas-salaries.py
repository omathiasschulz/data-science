# Pandas - Exercícios

# Dataset SF Salaries Dataset - Dataset Salarios de São Francisco
# Kaggle Dataset: https://www.kaggle.com/kaggle/sf-salaries

# Importar o pandas
import pandas as pd

# Ler o arquivo Salaries.csv como um DataFrame
sal = pd.read_csv('analise-dados/Salaries.csv')

# Verificar o "head" do DataFrame
print(sal.head())

# Descobrir quantas entradas existem
print(sal.info())


# Média de resultados da coluna BasePay
print(sal['BasePay'].mean())

# Maior quantidade de "OvertimePay" no conjunto de dados
print(sal['OvertimePay'].max())

# Cargo de JOSEPH DRISCOLL (tudo maíusculo)
print(sal[sal['EmployeeName'] == 'joseph driscoll'.upper()]['JobTitle'])

# Quanto JOSEPH DRISCOLL ganha (incluindo benefícios)
print(sal[sal['EmployeeName'] == 'joseph driscoll'.upper()]['TotalPayBenefits'])

# Nome da pessoa mais bem paga (incluindo benefícios)
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])

# Nome da pessoa com pior pagamento (incluindo benefícios)
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()][['EmployeeName','TotalPayBenefits']])

# Média de BasePay de todos os funcionários por ano (2011 - 2014)
print(sal[(sal['Year'] >= 2011) & (sal['Year'] <= 2014)].groupby('Year')['BasePay'].mean())

# Quantidade de títulos de trabalho únicos
print(sal['JobTitle'].nunique())

# Os 5 principais empregos mais comuns
print(sal['JobTitle'].value_counts().head(5))

# Títulos de Trabalho representados por apenas uma pessoa em 2013
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))

# Quantidade de pessoas que possuem a palavra Chefe em seu cargo
print(sum(sal['JobTitle'].str.contains('Chief', case=False)))
