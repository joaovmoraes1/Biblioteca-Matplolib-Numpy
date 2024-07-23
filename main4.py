import matplotlib.pyplot as plt
import numpy as np

# Gerando os dados do eixo x para serem plotados
x = np.arange(0, 5, 0.1)

# Gerando os dados do eixo y para serem plotados
y1 = x**2
y2 = x**5

# Usando o plt.subplots() para plotar vários gráficos em uma mesma figura.
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
plt.suptitle("Gráficos com Subplots")
plt.subplots_adjust(
    left=0.093,
    right=0.948,
    top=0.9,
    bottom=0.1,
    wspace=0.348,
    hspace=0.4
)

# Plotando os gráficos nos diferentes Axes e configurando
axes[0, 0].plot(x, y1)
axes[0, 0].set_title("Função do Segundo Grau $x^2$")
axes[0, 0].set_xlabel("Tempo")
axes[0, 0].set_ylabel("Amplitude")
axes[0, 0].grid(True)

axes[0, 1].plot(x, y2)
axes[0, 1].set_title("Função do Quinto Grau $x^5$")
axes[0, 1].set_xlabel("Tempo")
axes[0, 1].set_ylabel("Amplitude")
axes[0, 1].grid(True)

axes[1, 0].plot(x, y2)
axes[1, 0].set_title("Função do Quinto Grau $x^5$")
axes[1, 0].set_xlabel("Tempo")
axes[1, 0].set_ylabel("Amplitude")
axes[1, 0].grid(True)

axes[1, 1].plot(x, y1)
axes[1, 1].set_title("Função do Segundo Grau $x^2$")
axes[1, 1].set_xlabel("Tempo")
axes[1, 1].set_ylabel("Amplitude")
axes[1, 1].grid(True)

plt.show()
