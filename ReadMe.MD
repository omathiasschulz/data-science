# Python

Para as instalações, utilize sistema de gerenciamento de pacotes pip para Python 2 e o pip3 para Python 3



### Datasets de testes disponível no Kaggle

`https://www.kaggle.com/datasets`



# Análise de Dados



### Numpy

Numpy é uma biblioteca de álbegra linear para Python.

Numpy arrays essencialmente vêm de duas formas: vetores e matrizes.

É o bloco de construção de todas as outras bibliotecas de análise de dados.

É extremamente rápida, uma vez que seus principais métodos foram compilados em C.

##### Instalar a biblioteca NumPy

`pip install numpy`



### Pandas

Pandas é uma biblioteca código aberto escrito sobre o Numpy.

Permite rápida visualização e limpeza de dados.

É muito semelhante ao Excel.

Pode trabalhar com dados de diversos tipos diferentes.

Possui métodos próprios de visualização de dados.

##### Instalar a biblioteca Pandas

`pip install pandas`

##### Ler tabelas de uma página HTML

A função Pandas read_html irá ler tabelas de uma página da Web e retornar uma lista de objetos DataFrame.

Intalação:

`pip install lxml`

`pip install html5lib`

`pip install BeautifulSoup4`

Exemplo:

```
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df[0])
```



# Visualização de Dados



### Matplotlib

Matplotlib (https://matplotlib.org) é a biblioteca de visualização de dados mais popular do Python.

Exemplos de gráficos para serem implementados:

https://matplotlib.org/gallery/index.html

Possui métodos semelhantes aos métodos de plotagem gráfica do MatLab.

##### Instalar a biblioteca Matplotlib

`pip install matplotlib`



### Seaborn

É uma biblioteca para visualização estatística de dados

Possui excelentes estilos padrões

É baseado no matplotlib, no qual permite criar alguns tipos de gráficos de forma mais fácil quando comparado ao matplotlib
Foi projetada para funcionar em harmonia com objetos do tipo DataFrame do pandas

`pip install seaborn`

