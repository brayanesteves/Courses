# DataFrames : Modificación de los nombres de las filas
print("DataFrames : Modificación de los nombres de las filas\n")

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

nuevas_filas = 'dia1 dia2 dia3'.split()
print(nuevas_filas)
'''
['dia1', 'dia2', 'dia3']
'''

print()

dataframe['dias'] = nuevas_filas
print(dataframe)
'''
         zonaA  zonaB  zonaC  dias
ventas1    120    340    250  dia1
ventas2    210    450    250  dia2
ventas3    310    210    140  dia3
'''

print()

print(dataframe.set_index('dias'))
'''
      zonaA  zonaB  zonaC
dias
dia1    120    340    250
dia2    210    450    250
dia3    310    210    140
'''

print()

dataframe = dataframe.set_index('dias')
print(dataframe)
'''
      zonaA  zonaB  zonaC
dias
dia1    120    340    250
dia2    210    450    250
dia3    310    210    140
'''

print()