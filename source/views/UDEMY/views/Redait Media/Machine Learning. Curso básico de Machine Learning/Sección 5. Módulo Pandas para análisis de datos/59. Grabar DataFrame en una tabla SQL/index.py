# Pandas - SQL
# conda install sqlalchemy
# pip install sqlalchemy
print("Pandas - SQL\n")

import pandas as pd
from sqlalchemy import create_engine

diccionario = {'A': [1, 2, 3], 'B': [4, 5, 6]}
dataframe = pd.DataFrame(diccionario)
print(dataframe)
'''
   A  B
0  1  4
1  2  5
2  3  6
'''

print()

engine = create_engine('sqlite:///:memory:')
dataframe.to_sql('tabla', engine, index=False)
datos_leidos_bd = pd.read_sql('tabla', con=engine)
print(datos_leidos_bd)
'''
   A  B
0  1  4
1  2  5
2  3  6
'''