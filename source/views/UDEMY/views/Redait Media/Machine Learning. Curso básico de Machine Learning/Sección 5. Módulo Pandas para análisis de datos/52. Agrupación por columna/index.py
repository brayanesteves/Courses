# Pandas - Agrupación de datos
print("Pandas - Agrupación de datos\n")

import numpy as np
import pandas as pd

diccionario = {'dias': ['dia1', 'dia1', 'dia2', 'dia2', 'dia3'], 'vendedores': ['Antonio', 'Maria', 'Jose', 'Marta', 'Juan'], 'Ventas': [100, 400, 200, 500, 300]}
dataframe = pd.DataFrame(diccionario)
print(dataframe)
'''
   dias vendedores  Ventas
0  dia1    Antonio     100
1  dia1      Maria     400
2  dia2       Jose     200
3  dia2      Marta     500
4  dia3       Juan     300
'''

print()

print(dataframe.groupby('dias').mean())
'''
      Ventas
dias
dia1     250
dia2     350
dia3     300
'''

print()

print(dataframe.groupby('dias').sum())
'''
      Ventas
dias
dia1     500
dia2     700
dia3     300
'''

print()

print(dataframe.groupby('dias').describe())
'''
     Ventas
      count   mean         std    min    25%    50%    75%    max
dias
dia1    2.0  250.0  212.132034  100.0  175.0  250.0  325.0  400.0
dia2    2.0  350.0  212.132034  200.0  275.0  350.0  425.0  500.0
dia3    1.0  300.0         NaN  300.0  300.0  300.0  300.0  300.0
'''