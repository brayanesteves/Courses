# DataFrames : Selección de datos con una condición
print("DataFrames : Selección de datos con una condición\n")

import pandas as pd

filas = 'ventas1 ventas2 ventas3'.split()
print(filas)

print()

columnas = 'zonaA zonaB zonaC'.split()
print(columnas)

print()

datos = [[120, 340, 250], [210, 450, 250], [310, 210, 140]]
print(datos)

print()

dataframe = pd.DataFrame(datos, filas, columnas)
print(dataframe)
'''
         zonaA  zonaB  zonaC
ventas1    120    340    250
ventas2    210    450    250
ventas3    310    210    140
'''

print()

condicion = dataframe > 200
print(dataframe[condicion])
'''
         zonaA  zonaB  zonaC
ventas1    NaN    340  250.0
ventas2  210.0    450  250.0
ventas3  310.0    210    NaN
'''

print()

print(dataframe)
'''
         zonaA  zonaB  zonaC
ventas1    120    340    250
ventas2    210    450    250
ventas3    310    210    140
'''

print()

condicion = dataframe['zonaA'] > 200
print(dataframe[condicion])
'''
         zonaA  zonaB  zonaC
ventas2    210    450    250
ventas3    310    210    140
'''

print()

print(dataframe)
'''
         zonaA  zonaB  zonaC
ventas1    120    340    250
ventas2    210    450    250
ventas3    310    210    140
'''

print()

condicion = (dataframe['zonaA'] > 200) & (dataframe['zonaB'] > 300)
print(dataframe[condicion])
'''
         zonaA  zonaB  zonaC
ventas2    210    450    250
'''

print()

condicion = (dataframe['zonaA'] > 200) | (dataframe['zonaB'] > 300)
print(dataframe[condicion])
'''
         zonaA  zonaB  zonaC
ventas1    120    340    250
ventas2    210    450    250
ventas3    310    210    140
'''

print()

condicion = (dataframe['zonaA'] > 200) | (dataframe['zonaB'] > 300)
print(dataframe[condicion][['zonaB', 'zonaC']])
'''
         zonaB  zonaC
ventas1    340    250
ventas2    450    250
ventas3    210    140
'''