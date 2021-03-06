# Matplotlib
print("Matplotlib\n")

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2, 9, 10)
print(x)
'''
[2.         2.77777778 3.55555556 4.33333333 5.11111111 5.88888889
 6.66666667 7.44444444 8.22222222 9.        ]
'''

print()

y = x ** 2
print(y)
'''
[ 4.          7.71604938 12.64197531 18.77777778 26.12345679 34.67901235
 44.44444444 55.41975309 67.60493827 81.        ]
'''

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'red')
plt.show()

plt.plot(x, y, 'green')
plt.show()

plt.plot(x, y, 'lightgreen')
plt.show()

plt.plot(x, y, 'lightgreen')
plt.title('Este es mi gráfico')
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()

# 1 fila y 2 columnas
plt.subplot(1, 2, 1)
plt.plot(x, y, 'g')
# 1 fila y 2 columnas
plt.subplot(1, 2, 2)
plt.plot(y, x, 'blue')
plt.show()

# 2 filas y 1 columna
plt.subplot(2, 1, 1)
plt.plot(x, y, 'g')
# 2 filas y 1 columna
plt.subplot(2, 1, 2)
plt.plot(y, x, 'blue')
plt.show()

# Programación orientada a objetos
print("\nProgramación orientada a objetos\n")
figura  = plt.figure()
grafico = figura.add_axes([0.1, 0.1, 0.8, 0.8])
grafico.plot(x, y, 'green')
plt.show()

figura  = plt.figure()
grafico = figura.add_axes([0.1, 0.1, 1, 1])
grafico.plot(x, y, 'green')
plt.show()

figura  = plt.figure()
grafico1 = figura.add_axes([0.1, 0.1, 0.9, 0.9])
grafico1.plot(x, y, 'r')
grafico2 = figura.add_axes([0.2, 0.4, 0.3, 0.3])
grafico2.plot(y, x, 'blue')
plt.show()

figura  = plt.figure()
grafico1 = figura.add_axes([0.1, 0.1, 0.9, 0.9])
grafico1.plot(x, y, 'r')
grafico2 = figura.add_axes([0.2, 0.5, 0.3, 0.3])
grafico2.plot(y, x, 'blue')
plt.show()

figura  = plt.figure()
grafico1 = figura.add_axes([0.1, 0.1, 0.9, 0.9])
grafico1.plot(x, y, 'r')
grafico2 = figura.add_axes([0.2, 0.5, 0.3, 0.4])
grafico2.plot(y, x, 'blue')
plt.show()

figura  = plt.figure()
grafico1 = figura.add_axes([0.1, 0.1, 0.9, 0.9])
grafico1.plot(x, y, 'r')
grafico2 = figura.add_axes([0.2, 0.5, 0.4, 0.4])
grafico2.plot(y, x, 'blue')
plt.show()

# Multigráficos (filas, columnas)
print("\nMultigráficos (filas, columnas)\n")

figura, graficos = plt.subplots(nrows=2, ncols=2)
plt.show()

figura, graficos = plt.subplots(nrows=4, ncols=3)
plt.show()

figura, graficos = plt.subplots(nrows=2, ncols=2)
plt.show()

figura, graficos = plt.subplots(nrows=2, ncols=2)
graficos[0][0].plot(x, y, 'blue')
plt.show()

figura, graficos = plt.subplots(nrows=2, ncols=2)
graficos[0][0].plot(x, y, 'blue')
graficos[0][1].plot(x, y, 'red')
graficos[1][0].plot(x, y, 'y')
graficos[1][1].plot(x, y, 'g')
plt.show()

figura, graficos = plt.subplots(nrows=2, ncols=2)
graficos[0][0].plot(x, y, 'blue')
graficos[0][1].plot(x, y, 'red')
graficos[1][0].plot(x, y, 'y')
graficos[1][1].plot(x, y, 'g')

graficos[0][0].set_title('Azul')
graficos[0][1].set_title('Rojo')
graficos[1][0].set_title('Amarillo')
graficos[1][1].set_title('Verde')
plt.show()

# Tamaño del gráfico
print("\nTamaño del gráfico\n")

figura  = plt.figure(figsize=(8, 4))
grafico = figura.add_axes([0.1, 0.1, 0.9, 0.9])
grafico.plot(x, y, 'r')
plt.show()

figura  = plt.figure(figsize=(8, 2))
grafico = figura.add_axes([0.1, 0.1, 0.9, 0.9])
grafico.plot(x, y, 'r')
plt.show()

figura  = plt.figure(figsize=(10, 2))
grafico = figura.add_axes([0.1, 0.1, 0.9, 0.9])
grafico.plot(x, y, 'r')
plt.show()