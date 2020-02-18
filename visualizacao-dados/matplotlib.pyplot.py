# Importando matplotlib.pyplot
import matplotlib.pyplot as plt

# Criando dados de exemplo
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2

# Criar um objeto de figura
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_xlabel('Label X')
ax.set_ylabel('Label Y')
ax.set_title('Título')
plt.show()

# Objeto de figura com dois eixos
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = fig.add_axes([0.25, 0.6, .2, .2])
ax1.plot(x, y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.plot(x, y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.show()

# Criar um objeto de figura
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.plot(x, z)
ax2 = fig.add_axes([.22, .46, .35, .35])
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('zoom')
ax2.plot(x, y)
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)
plt.show()

# Criar um objeto de figura
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y, color='blue', lw=3, ls='--', label='Legenda 01')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].set_title('Título 01')
# axes[0].legend(loc=1) # Canto superior direito
# axes[0].legend(loc=2) # Canto superior esquerdo
# axes[0].legend(loc=3) # Canto inferior esquerdo
# axes[0].legend(loc=4) # Canto inferior direito
axes[0].legend(loc=0) # Ajuste automático da legenda
axes[1].plot(x, z, color='red', lw=3, ls='-', label='Legenda 02')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')
axes[1].set_title('Título 02')
axes[1].legend(loc=0)
# Ajustar a sobreposição de subplots ou figuras
plt.tight_layout()
plt.show()

# Salvar uma figura
fig.savefig("visualizacao-dados/images/figure01.png")

# Ajustando a qualidade da imagem
fig.savefig("visualizacao-dados/images/figure02.png", dpi=200)
fig.savefig("visualizacao-dados/images/figure03.png", dpi=1000)

# Redimencionar
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))
axes[0].plot(x, y, color='blue', lw=3, ls='--')
axes[1].plot(x, z, color='red', lw=3, ls='-')
plt.show()

# Cor e estilo da linha como MATLAB
fig, ax = plt.subplots()
ax.plot(x, x**2, 'b.-') # linha azul tracejada
ax.plot(x, x**3, 'g--', alpha=0.5) # linha verde pontilhada e meio transparente
plt.show()
