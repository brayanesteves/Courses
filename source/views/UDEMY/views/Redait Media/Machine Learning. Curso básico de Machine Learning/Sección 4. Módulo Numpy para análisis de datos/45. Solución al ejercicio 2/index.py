# Ejercicio

'''
Crea un "array" de una dimensión con 9 valores enteros aleatorios entre 0 y 100
Convierte ese "array" en un matriz de 2 dimensiones (3 Filas y 3 Columnas)
Muestra por pantalla el valor del elemento de la matriz, de la esquina inferior derecha
'''

import numpy as np

array = np.random.randint(0, 100, 9)
print(array)
'''
Crea un "array" de una dimensión con 9 valores enteros aleatorios entre 0 y 100

[94 82 52 89 34 69 78 33 46]
'''

print()

'''
3 Filas & 3 Columnas
'''
matriz = array.reshape(3, 3)
print(matriz)
'''
Convierte ese "array" en un matriz de 2 dimensiones (3 Filas y 3 Columnas)

[[57 36 72]
 [42 15 39]
 [ 3 98 55]]
'''

print()

print(matriz[2][2])
'''
Muestra por pantalla el valor del elemento de la matriz, de la esquina inferior derecha

93
'''