# Series
print("Series\n")

import numpy as np
import pandas as pd

etiquetas = ['a', 'b', 'c']
datos = [1, 2, 3]

print(pd.Series(data=datos, index=etiquetas))
'''
a    1
b    2
c    3
dtype: int64
'''

print()

array = np.arange(0, 3)
print(pd.Series(array))
'''
0    0
1    1
2    2
dtype: int32
'''

print()

array = np.arange(5, 8)
print(pd.Series(array))
'''
0    5
1    6
2    7
dtype: int32
'''

print()

array = np.arange(5, 8)
etiqueta = ['venta1', 'venta2', 'venta3']
print(pd.Series(array, etiqueta))
'''
venta1    5
venta2    6
venta3    7
dtype: int32
'''

print()

array = np.arange(5, 8)
etiqueta = ['venta1', 'venta2', 'venta3']
serie1 = pd.Series(array, etiqueta)
print(serie1)
'''
venta1    5
venta2    6
venta3    7
dtype: int32
'''

print()

print(serie1['venta1'])
'''
5
'''

print()

print(serie1['venta2'])
'''
6
'''

print()

print(serie1[2])
'''
7
'''

print()

print(serie1[1])
'''
6
'''

print()

datos2 = ['informatica', 300, 'impresora', 400]
print(pd.Series(datos2))
'''
0    informatica
1            300
2      impresora
3            400
dtype: object
'''

print()

serie1 = pd.Series([1, 2, 3], ['ventas1', 'ventas2', 'ventas3'])
serie2 = pd.Series([4, 8, 5], ['ventas1', 'ventas2', 'ventas3'])
serie_suma = serie1 + serie2
print(serie_suma)
'''
ventas1     5
ventas2    10
ventas3     8
dtype: int64
'''

print()

print(serie1)
'''
ventas1    1
ventas2    2
ventas3    3
dtype: int64
'''

print()

print(serie2)
'''
ventas1    4
ventas2    8
ventas3    5
dtype: int64
'''

print()

print()

serie1 = pd.Series([1, 2, 3, 4], ['ventas1', 'ventas2', 'ventas3', 'ventas4'])
serie2 = pd.Series([4, 8, 5], ['ventas1', 'ventas2', 'ventas3'])
serie_suma = serie1 + serie2
print(serie_suma)
'''
ventas1     5.0
ventas2    10.0
ventas3     8.0
ventas4     NaN
dtype: float64
'''

print()

print(serie1)
'''
ventas1    1
ventas2    2
ventas3    3
ventas4    4
dtype: int64
'''

print()

print(serie2)
'''
ventas1    4
ventas2    8
ventas3    5
dtype: int64
'''

print()