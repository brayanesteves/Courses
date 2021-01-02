# Pandas - Merge DataFrames
print("Pandas - Merge DataFrames\n")

import numpy as np
import pandas as pd

diccionario = {'A': [1, 2, 3], 'B': [4, 5, 6], 'Clave': ['c1', 'c2', 'c3']}
dataframe1 = pd.DataFrame(diccionario)
print(dataframe1)
'''
   A  B Clave
0  1  4    c1
1  2  5    c2
2  3  6    c3
'''

print()

diccionario2 = {'C': [11, 12, 13], 'D': [14, 15, 16], 'Clave': ['c1', 'c2', 'c3']}
dataframe2 = pd.DataFrame(diccionario2)
print(dataframe2)
'''
    C   D Clave
0  11  14    c1
1  12  15    c2
2  13  16    c3
'''

print()

print(pd.merge(dataframe1, dataframe2, on = 'Clave'))
'''
   A  B Clave   C   D
0  1  4    c1  11  14
1  2  5    c2  12  15
2  3  6    c3  13  16
'''