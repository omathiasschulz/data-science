# Python

# 7 elevado na potência 4
print(7**4)

# Quebrar uma string
string = 'Mathias Artur Schulz'
print(string.split())

# Formatar uma string
planeta = "Terra"
diametro = 12742
print("O diâmetro da {} é de {} kilômetros".format(planeta, diametro))

# Buscar a palavra olá em um array multidimencional
array = [1,2,[3,4],[5,[100,200,['olá']],23,11],1,7]
print(array[3][1][2][0])

# Buscar a palavra olá em um dicionário multidimencional
array = {'k1':[1,2,3,{'café':['banana','mulher','colher',{'alvo':[1,2,3,'olá']}]}]}
print(array['k1'][3]['café'][3]['alvo'][3])

# Obter o domínio de um email
def obterDominio(string):
    return string.split('@')[1]
print(obterDominio('mathias@mathias.com.br'))

# Buscar uma palavra em uma string
def encontrarPalavra(string):
    return 'fulano' in string.lower().split()
encontrarPalavra('Nome nome é fulano da cidade x')

# Utilizando lambda e filter
# lambda => Representa uma função anônima, sem nome, utilizada apenas na sua criação
# filter => Permite iterar sobre um array e executar uma determinada operação e 
# retorna todos os elementos que foram true
# Buscar palavras que iniciam com 's'
array = ['sopa', 'cachorro', 'salada', 'gato', 'ótimo']
print(list(filter(lambda palavra : palavra[0] == 's', array)))
