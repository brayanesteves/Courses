# Ejercicio

'''
El objetivo será crear un dataframe con las ventas de nuestras 3 oficinas para los meses de enero, febrero y marzo.
Pasos a seguir:
Crea una variable "ventas_enero" que contenga una lista de 3 números enteros aleatorios entre 100 y 500
Crea una variable "ventas_febrero" que contenga una lista de 3 números enteros aleatorios entre 100 y 500
Crea una variable "ventas_marzo" que contenga una lista de números enteros aleatorios entre 100 y 500
Crea una variable "filas" que contenga esta lista de palabras : 'ventas_enero', 'ventas_febrero', 'ventas_marzo'
Crea una variable "columnas" que contenga esta lista de palabras : 'oficina_1', 'oficina_2', 'oficina_3'
Crea una variable "ventas" que contenga una lista con los valores de ventas de enero, febrero y marzo
Crea una variable "dataframe" que contenga las ventas, filas y columnas
Mediante "print" muestra el valor de "Las ventas de enero para la oficina 1 son de ....."
'''

import numpy as np
import pandas as pd

ventas_enero = np.random.randint(100, 500, 3)
print(ventas_enero)

print()

ventas_febrero = np.random.randint(100, 500, 3)
print(ventas_febrero)

print()

ventas_marzo = np.random.randint(100, 500, 3)
print(ventas_marzo)

print()

filas = ['ventas_enero', 'ventas_febrero', 'ventas_marzo']
print(filas)

print()

columnas = ['oficina_1', 'oficina_2', 'oficina_3']
print(columnas)

print()

ventas = [ventas_enero, ventas_febrero, ventas_marzo]
print(ventas)

print()

dataframe = pd.DataFrame(ventas, filas, columnas)
print(dataframe)
'''
                oficina_1  oficina_2  oficina_3
ventas_enero          302        483        293
ventas_febrero        396        358        469
ventas_marzo          480        228        455
'''

print()

ventas_enero_oficina_1 = dataframe['oficina_1']['ventas_enero']
print(ventas_enero_oficina_1)
print("Las ventas de enero de la oficina_1 son de {}".format(ventas_enero_oficina_1))