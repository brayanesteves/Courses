# DataFrames
print("DataFrames\n")

import numpy as np
import pandas as pd

filas = ['ventas1', 'ventas2', 'ventas3']
columnas = ['zonaA', 'zonaB', 'zonaC']
datos = [[123, 421, 256], [234, 541, 257], [120, 451, 258]]

dataframes = pd.DataFrame(datos, filas, columnas)
print(dataframes)
'''
         zonaA  zonaB  zonaC
ventas1    123    421    256
ventas2    234    541    257
ventas3    120    451    258
'''

print()

print(dataframes.loc['ventas1'])
'''
zonaA    123
zonaB    421
zonaC    256
Name: ventas1, dtype: int64
'''

print()

print(dataframes.loc[['ventas1', 'ventas2']])
'''
         zonaA  zonaB  zonaC
ventas1    123    421    256
ventas2    234    541    257
'''

print()

print(dataframes['zonaA'])
'''
ventas1    123
ventas2    234
ventas3    120
Name: zonaA, dtype: int64
'''

print()

print(dataframes[['zonaA', 'zonaC']])
'''
         zonaA  zonaC
ventas1    123    256
ventas2    234    257
ventas3    120    258
'''

print()

print(dataframes.loc['ventas1']['zonaA'])
'''
123
'''

print()

dataframes['Todaslaszonas'] = dataframes['zonaA'] + dataframes['zonaB'] + dataframes['zonaC']
print(dataframes)
'''
         zonaA  zonaB  zonaC  Todaslaszonas
ventas1    123    421    256            800
ventas2    234    541    257           1032
ventas3    120    451    258            829
'''

print()

'''
axis = 1 (Significa 1 columna)
inplace = True (Significa para borrarlo en definitiva)
'''
dataframes.drop('Todaslaszonas', axis = 1, inplace = True)
print(dataframes)
'''
         zonaA  zonaB  zonaC
ventas1    123    421    256
ventas2    234    541    257
ventas3    120    451    258
'''

print()

'''
inplace = True (Significa para borrarlo en definitiva)
'''
dataframes.drop('ventas3', inplace = True)
print(dataframes)
'''
         zonaA  zonaB  zonaC
ventas1    123    421    256
ventas2    234    541    257
'''

print()

print(dataframes.shape)
'''
(2, 3)
'''