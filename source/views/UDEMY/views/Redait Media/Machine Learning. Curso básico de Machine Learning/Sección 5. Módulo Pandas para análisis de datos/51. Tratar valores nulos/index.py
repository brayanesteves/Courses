# Pandas : Tratamiento datos nulos o sin valor
print("Pandas : Tratamiento datos nulos o sin valor\n")

import numpy as np
import pandas as pd

'''
np.nan, representa un valor NULL
'''
diccionario = {'A': [4, 5, np.nan], 'B': [6, 1, 5], 'C': [np.nan, 4, np.nan]}
dataframe = pd.DataFrame(diccionario)
print(dataframe)
'''
     A  B    C
0  4.0  6  NaN
1  5.0  1  4.0
2  NaN  5  NaN
'''

print()

print(dataframe.dropna())
'''
     A  B    C
1  5.0  1  4.0
'''

print()

print(dataframe.dropna(axis = 1))
'''
   B
0  6
1  1
2  5
'''

print()

dataframe.dropna(axis = 1, inplace=True)
print(dataframe)
'''
   B
0  6
1  1
2  5
'''

print()

diccionario = {'A': [4, 5, np.nan], 'B': [6, 1, 5], 'C': [np.nan, 4, np.nan]}
dataframe = pd.DataFrame(diccionario)
dataframe.fillna(value=100, inplace=True)
print(dataframe)
'''
       A  B      C
0    4.0  6  100.0
1    5.0  1    4.0
2  100.0  5  100.0
'''

print()

diccionario = {'A': [4, 5, np.nan], 'B': [6, 1, 5], 'C': [np.nan, 4, np.nan]}
dataframe = pd.DataFrame(diccionario)
dataframe.fillna(value=100)
valor_medio = dataframe.mean()
print(valor_medio)
'''
A    4.5
B    4.0
C    4.0
dtype: float64
'''

print()

dataframe.fillna(value=valor_medio)
print(dataframe)