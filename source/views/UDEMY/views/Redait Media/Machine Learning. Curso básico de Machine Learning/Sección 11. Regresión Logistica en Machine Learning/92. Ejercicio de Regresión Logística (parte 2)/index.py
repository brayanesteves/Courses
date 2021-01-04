# Ejemplo regresión logística
print("Ejemplo regresión logística\n")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

entrenamiento = pd.read_csv('train.csv')

# Limpieza de datos
print("Limpieza de datos\n")

entrenamiento.head()
entrenamiento.isnull()

sns.heatmap(entrenamiento.isnull())

sns.boxplot(x='Pclass', y='Age', data=entrenamiento)

def edad_media(columnas):
    edad  = columnas[0]
    clase = columnas[1]
    if pd.isnull(edad):
        if clase == 1:
            return 38
        elif clase == 2:
            return 30
        else:
            return 25
    else:
        return edad

entrenamiento['Age'] = entrenamiento[['Age', 'Pclass']].apply(edad_media, axis=1)

entrenamiento.head()
entrenamiento.isnull()

entrenamiento.drop('Cabin', axis=1, inplace=True)

entrenamiento.head()
entrenamiento.isnull()

entrenamiento.head()

entrenamiento.drop(['Name', 'Ticket', 'PassengerId'], axis=1, inplace=True)
entrenamiento.head()

pd.get_dummies(entrenamiento['Sex'])
pd.get_dummies(entrenamiento['Sex'], drop_first=True)

sexo = pd.get_dummies(entrenamiento['Sex'], drop_first=True)

entrenamiento = pd.concat([entrenamiento, sexo], axis=1)
entrenamiento.head()

entrenamiento.drop('Sex', axis=1, inplace=True)
entrenamiento.head()

puerto = pd.get_dummies(entrenamiento['Embarked'])
print(puerto)
'''
     C  Q  S
0    0  0  1
1    1  0  0
2    0  0  1
3    0  0  1
4    0  0  1
..  .. .. ..
886  0  0  1
887  0  0  1
888  0  0  1
889  1  0  0
890  0  1  0

[891 rows x 3 columns]
'''

print()

puerto = pd.get_dummies(entrenamiento['Embarked'], drop_first=True)
print(puerto)
'''
     Q  S
0    0  1
1    0  0
2    0  1
3    0  1
4    0  1
..  .. ..
886  0  1
887  0  1
888  0  1
889  0  0
890  1  0

[891 rows x 2 columns]
'''

entrenamiento = pd.concat([entrenamiento, puerto], axis=1)
entrenamiento.head()

entrenamiento.drop('Embarked', axis=1, inplace=True)
entrenamiento.head()