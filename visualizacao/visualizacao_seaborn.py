# Seaborn

import matplotlib.pyplot as plt
import seaborn as sns

# Conjunto de dados do Titanic
titanic = sns.load_dataset('titanic')
# Apresentando o dataset
print(titanic.head())
# Apresenta as colunas
print(titanic.head())

# Setando um estilo padrão
sns.set_style('whitegrid')

# Visualizar a distribuição dos dados
# Apresenta o preço da tarifa de acordo com a idade
sns.jointplot(x='fare', y='age', data=titanic)
plt.show()

sns.distplot(titanic['fare'], kde=False, color='red', bins=30)
plt.show()
