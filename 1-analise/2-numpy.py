# NumPy

# Importar NumPy
import numpy as np

# Matriz de 10 zeros
array = np.zeros(10)
print(array)

# Matriz de 10 ums
array = np.ones(10)
print(array)

# Matriz de 10 cincos
array = np.ones(10) * 5
print(array)

# Array de inteiros de 10 até 50
array = np.arange(10, 51)
print(array)

# Array de números pares de 10 até 50
array = np.arange(10, 51, 2)
print(array)

# Matriz 3x3 com valores variando de 0 até 8
array = np.arange(9).reshape(3,3)
print(array)

# Matriz identidade 3x3
array = np.eye(3)
print(array)

# Números aleatórios entre 0 e 1
value = np.random.rand()
print(value)

# Array de 25 números aleatórios tirados de uma distribuição normal.
array = np.random.randn(25)
print(array)

# Criação de uma matriz
array = np.arange(0.1, 1, 0.01).reshape(9,10)
print(array)

# Array de tamanho 20 igualmente espaçado entre 0 e 1.
array = np.linspace(0, 1, 20)
print(array)

# Criação de uma matriz
mat = np.arange(1,26).reshape(5,5)
print(mat)

# Buscando 'pedaços' da matriz
print(mat[2:,1:])
print(mat[3,4])
print(mat[:3,1:2])
print(mat[4])
print(mat[3:])

# Soma de todos os valores no array mat - Duas formas:
print(np.sum(mat))
print(mat.sum())

# Desvio padrão dos valores no array mat
print(mat.std())

# Soma de todas as colunas no array mat
print(mat.sum(axis=0))
