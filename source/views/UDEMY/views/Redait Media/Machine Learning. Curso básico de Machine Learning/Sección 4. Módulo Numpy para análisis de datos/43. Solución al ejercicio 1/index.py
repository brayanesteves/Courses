# Ejercicio

'''
Crea una lista de números secuenciales con el valor mínimo de 10 y el valor máximo 39
Convierte esta lista en una lista o matriz de 2 dimensiones (3 filas por 10 columnas)
Muestra por pantalla el valor del elemento de la esquina superior derecha de la matriz 
'''
import numpy as np

'''
Crea una lista de números secuenciales con el valor mínimo de 10 y el valor máximo 39
'''
lista = np.arange(10, 40)
print(lista)

print()

'''
Convierte esta lista en una lista o matriz de 2 dimensiones (3 filas por 10 columnas)
3 Filas y 10 Columnas
'''
lista = lista.reshape(3, 10)
print(lista)
'''
Muestra por pantalla el valor del elemento de la esquina superior derecha de la matriz
[[10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29]
 [30 31 32 33 34 35 36 37 38 39]]
'''

print()

print(lista[0][9])