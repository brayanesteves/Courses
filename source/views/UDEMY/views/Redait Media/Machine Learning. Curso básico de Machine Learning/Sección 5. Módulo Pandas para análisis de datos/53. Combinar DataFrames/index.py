# Pandas - Combinar DataFrames
print("Pandas - Combinar DataFrames\n")

import numpy as np
import pandas as pd

diccionario = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
dataframe1 = pd.DataFrame(diccionario)
print(dataframe1)
'''
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
'''

print()

diccionario2 = {'A': [11, 12, 13], 'B': [14, 15, 16], 'C': [17, 18, 19]}
dataframe2 = pd.DataFrame(diccionario2)
print(dataframe2)
'''
    A   B   C
0  11  14  17
1  12  15  18
2  13  16  19
'''

print()

print(pd.concat([dataframe1, dataframe2]))
'''
    A   B   C
0   1   4   7
1   2   5   8
2   3   6   9
0  11  14  17
1  12  15  18
2  13  16  19
'''

print()

'''
axis = 1 (Eje 1)
'''
print(pd.concat([dataframe1, dataframe2], axis = 1))
'''
   A  B  C   A   B   C
0  1  4  7  11  14  17
1  2  5  8  12  15  18
2  3  6  9  13  16  19
'''