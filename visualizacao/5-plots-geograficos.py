import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, plot, iplot



# Choropleth US Maps
# Dicionário de dados
data = dict(
    type = 'choropleth', # Tipo de gráfico
    locations = ['AZ','CA','NY'], # Estados visíveis
    locationmode = 'USA-states', # Qual informação será buscada
    colorscale = 'Portland', # Tipo de cor a ser utilizada
    text = ['Texto1','Texto2','Texto3'], # Texto que aparece em cada estado
    z = [1.0,2.0,3.0], # Níveis de cores utilizados
    colorbar = {'title':'Título da barra de cores'} # Título
)

# Criação do dicionário de layout aninhado
layout = dict(geo = {'scope':'usa'})

# Configuração do objeto
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)



# Dados reais: Mapa dos EUA Choropleth
df = pd.read_csv('visualizacao/df/2011_US_AGRI_Exports')
print(df.head())

# Dicionário de dados
# Com argumentos adicionais e argumentos de barras de cores
data = dict(
    type ='choropleth',
    colorscale = 'greens',
    locations = df['code'],
    z = df['total exports'],
    locationmode = 'USA-states',
    text = df['text'],
    marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)), # Altera a cor e comprimento das bordas dos estados
    colorbar = {'title':"Milhões de dólares"}
) 

# Criação do dicionário de layout aninhado
# Alguns argumentos novos
layout = dict(title = '2011 Exportações de Agricultura dos EUA por Estado',
    geo = dict(scope='usa',
        showlakes = True, # Mostra os lagos
        lakecolor = 'rgb(85,173,240)' # Cor dos lagos
    )
)

# Configuração do objeto
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)



# Mapa-mundi Choropleth referente ao PIB mundial
df = pd.read_csv('visualizacao/df/2014_World_GDP')
print(df.head())

# Dicionário de dados
data = dict(
    type = 'choropleth', # Tipo de gráfico
    locations = df['CODE'], # Países com as cores
    z = df['GDP (BILLIONS)'], # Nível da cor
    text = df['COUNTRY'], # Texto para cada país
    colorbar = {'title' : 'GDP Billions US'}, # Título da barra de cores
)

# Criação do dicionário de layout aninhado
layout = dict(
    title = 'PIB do mundo em 2014',
    geo = dict(
        showframe = False, # Remove a borda do gráfico
        projection = {'type':'natural earth'} # Formato do mapa
    )
)

# Configuração do objeto
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)



# Mais informações sobre como usar o Plotly 
# https://plotly.com/python/

# Documentação Mapas Choropleth  
# https://plot.ly/python/reference/#choropleth)



# Mapa geográfico mundial sobre o consumo de energia no ano de 2014
# Visualizando o arquivo csv: 2014_World_Power_Consumption
df = pd.read_csv('visualizacao/df/2014_World_Power_Consumption')
print(df.head())

data = {
    'type': 'choropleth', # Tipo de mapa
    'colorscale': 'Viridis', # Cores do mapa
    'locations': df['Country'], # Estados que possuirão cor
    'locationmode':'country names', # Determina o que são as locations
    'z': df['Power Consumption KWH'], # Intensidade da cor de acordo com o valor
    'text': df['Text'], # Texto que aparece em cada estado
    'colorbar': {'title': 'Consumo de energia em KWH'},
}

layout = {
    'title': 'Consumo mundial de energia (2014)',
    'geo': {
        'showframe': False, # Sem bordas no mapa
        'projection': {'type': 'mercator'},
        'showlakes': True, # Mostrar os lagos
        'lakecolor': 'rgb(85, 173, 240)', # Cor dos lagos
    },
}

choromap = go.Figure(data = [data], layout = layout)
iplot(choromap, validate=False)



# Choropleth EUA Voting-Age Population (2012)
df = pd.read_csv('visualizacao/df/2012_Election_Data')
print(df.head())
print(df.info())

data = {
    'type': 'choropleth',
    'colorscale': 'Viridis',
    'locations': df['State Abv'],
    'locationmode': 'USA-states',
    'z': df['Voting-Age Population (VAP)'],
    'text': df['State'] + ' ' + df['State Abv'],
    'colorbar': {'title': 'Voting age population'}
}

layout = {
    'title': 'EUA Voting-Age Population (2012)',
    'geo': {
        'scope': 'usa', # Qual a região do mundo
        'showlakes': True,
    }
}

choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


