# Pandas - Operaciones
print("Pandas - Operaciones\n")

import numpy as np
import pandas as pd

diccionario = {'A': [11, 12, 10, 12], 'B': [14, 18, 16, 17]}
dataframe = pd.DataFrame(diccionario, index=['i1', 'i2', 'i3', 'i4'])
print(dataframe)
'''
     A   B
i1  11  14
i2  12  18
i3  10  16
i4  12  17
'''

print()

print(dataframe['A'].unique())
'''
[11 12 10]
'''

print()

print(dataframe['A'].nunique())
'''
3
'''

print()

print(dataframe['A'].value_counts())
'''
12    2
11    1
10    1
Name: A, dtype: int64
'''

print()

def multiplicar(x):
    return x * 2

print(dataframe['A'].apply(multiplicar))
'''
i1    22
i2    24
i3    20
i4    24
Name: A, dtype: int64
'''

print()

print(dataframe['A'].apply(lambda x: x * 2))
'''
i1    22
i2    24
i3    20
i4    24
Name: A, dtype: int64
'''

print()

print(dataframe.drop('B', axis = 1))
'''
     A
i1  11
i2  12
i3  10
i4  12
'''

print()

print(dataframe.drop('i1'))
'''
     A   B
i2  12  18
i3  10  16
i4  12  17
'''

print()

print(dataframe.columns)
'''
Index(['A', 'B'], dtype='object')
'''

print()

print(dataframe.index)
'''
Index(['i1', 'i2', 'i3', 'i4'], dtype='object')
'''

print()

print(dataframe.sort_values('B'))
'''
     A   B
i1  11  14
i3  10  16
i4  12  17
i2  12  18
'''