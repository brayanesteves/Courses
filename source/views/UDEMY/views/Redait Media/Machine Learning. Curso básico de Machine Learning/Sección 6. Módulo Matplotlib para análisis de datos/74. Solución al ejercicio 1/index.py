# Ejercicio

'''
Crear una variable "x" que tenga 10 valores equidistantes entre los valores 0 y 20
Crear una variable "y" que tenga los valores de la función "x al cuadrado + 5"
Crear un gráfico de color rojo, con ancho de 5 y estilo de puntos "...."
'''

import numpy as np
import matplotlib.pyplot as plt

# Crear una variable "x" que tenga 10 valores equidistantes entre los valores 0 y 20
x = np.linspace(0, 20, 10)
print(x)

print()

# Crear una variable "y" que tenga los valores de la función "x al cuadrado + 5"
y = (x ** 2) + 5
print(y)

print()

# Crear un gráfico de color rojo, con ancho de 5 y estilo de puntos "...."
plt.plot(x, y, 'red', linestyle=':', linewidth=5)
plt.show()