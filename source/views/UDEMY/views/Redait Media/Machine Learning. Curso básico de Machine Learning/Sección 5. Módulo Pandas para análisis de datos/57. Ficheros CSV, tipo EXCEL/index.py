# Pandas - Ficheros EXCEL
print("Pandas - Ficheros EXCEL\n")

import pandas as pd

dataframe = pd.read_excel("Sección 5. Módulo Pandas para análisis de datos/57. Ficheros CSV, tipo EXCEL/Ejemplo_excel.xls")
print(dataframe)
'''
   Unnamed: 0   a   b   c   d
0           0   0   1   2   3
1           1   4   5   6   7
2           2   8   9  10  11
3           3  12  13  14  15
'''

print()

dataframe['e'] = [20, 21, 22, 23]
print(dataframe)
'''
   Unnamed: 0   a   b   c   d   e
0           0   0   1   2   3  20
1           1   4   5   6   7  21
2           2   8   9  10  11  22
3           3  12  13  14  15  23
'''

print()

'''
Creamos un Excel
'salida_excel.xlsx' (Nombre del archivo a crear <Se puede crear cualquier nombre>)
sheet_name='Hoja' (Es el nombre de la hoja que tendra el Excel)
Y copia a es excel estos parametros

dataframe['e'] = [20, 21, 22, 23]
print(dataframe)
   Unnamed: 0   a   b   c   d   e
0           0   0   1   2   3  20
1           1   4   5   6   7  21
2           2   8   9  10  11  22
3           3  12  13  14  15  23
'''
dataframe.to_excel('Sección 5. Módulo Pandas para análisis de datos/57. Ficheros CSV, tipo EXCEL/salida_excel.xls', sheet_name='Hoja1')
