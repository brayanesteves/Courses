# Pandas - Join DataFrames
print("Pandas - Join DataFrames\n")

import numpy as np
import pandas as pd

diccionario = {'A': [1, 2, 3], 'B': [4, 5, 6]}
dataframe1 = pd.DataFrame(diccionario)
print(dataframe1)
'''
   A  B
0  1  4
1  2  5
2  3  6
'''

print()

diccionario = {'A': [1, 2, 3], 'B': [4, 5, 6]}
dataframe1 = pd.DataFrame(diccionario, index=['i1', 'i2', 'i3'])
print(dataframe1)
'''
    A  B
i1  1  4
i2  2  5
i3  3  6
'''

print()

diccionario2 = {'C': [11, 12, 13], 'D': [14, 15, 16]}
dataframe2 = pd.DataFrame(diccionario2, index=['i1', 'i2', 'i3'])
print(dataframe2)
'''
    A  B
i1  1  4
i2  2  5
i3  3  6
'''

print()

print(dataframe1.join(dataframe2))
'''
    A  B   C   D
i1  1  4  11  14
i2  2  5  12  15
i3  3  6  13  16
'''