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

# Entrenamiento del modelo
print("\nEntrenamiento del modelo\n")

entrenamiento.head()

y = entrenamiento['Survived']
X = entrenamiento.drop('Survived', axis=1)
print(X)
'''
     Pclass   Age  SibSp  Parch     Fare  male  Q  S
0         3  22.0      1      0   7.2500     1  0  1
1         1  38.0      1      0  71.2833     0  0  0
2         3  26.0      0      0   7.9250     0  0  1
3         1  35.0      1      0  53.1000     0  0  1
4         3  35.0      0      0   8.0500     1  0  1
..      ...   ...    ...    ...      ...   ... .. ..
886       2  27.0      0      0  13.0000     1  0  1
887       1  19.0      0      0  30.0000     0  0  1
888       3  25.0      1      2  23.4500     0  0  1
889       1  26.0      0      0  30.0000     1  0  0
890       3  32.0      0      0   7.7500     1  1  0

[891 rows x 8 columns]
'''
print()

print(y)
'''
0      0
1      1
2      1
3      1
4      0
      ..
886    0
887    1
888    0
889    1
890    0
Name: Survived, Length: 891, dtype: int64
'''

print()

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=45)

print(X_train)
'''
     Pclass   Age  SibSp  Parch      Fare  male  Q  S
650       3  25.0      0      0    7.8958     1  0  1
784       3  25.0      0      0    7.0500     1  0  1
125       3  12.0      1      0   11.2417     1  0  0
54        1  65.0      0      1   61.9792     1  0  0
446       2  13.0      0      1   19.5000     0  0  1
..      ...   ...    ...    ...       ...   ... .. ..
725       3  20.0      0      0    8.6625     1  0  1
607       1  27.0      0      0   30.5000     1  0  1
544       1  50.0      1      0  106.4250     1  0  0
643       3  25.0      0      0   56.4958     1  0  1
414       3  44.0      0      0    7.9250     1  0  1

[623 rows x 8 columns]
'''

print()

print(X_test)
'''
     Pclass   Age  SibSp  Parch     Fare  male  Q  S
248       1  37.0      1      1  52.5542     1  0  1
197       3  42.0      0      1   8.4042     1  0  1
133       2  29.0      1      0  26.0000     0  0  1
169       3  28.0      0      0  56.4958     1  0  1
736       3  48.0      1      3  34.3750     0  0  1
..      ...   ...    ...    ...      ...   ... .. ..
422       3  29.0      0      0   7.8750     1  0  1
815       1  38.0      0      0   0.0000     1  0  1
466       2  30.0      0      0   0.0000     1  0  1
559       3  36.0      1      0  17.4000     0  0  1
6         1  54.0      0      0  51.8625     1  0  1

[268 rows x 8 columns]
'''

print()

print(Y_train)
'''
650    0
784    0
125    1
54     0
446    1
      ..
725    0
607    1
544    0
643    1
414    1
Name: Survived, Length: 623, dtype: int64
'''

print()

print(Y_test)
'''
248    1
197    0
133    1
169    0
736    0
      ..
422    0
815    0
466    0
559    1
6      0
Name: Survived, Length: 268, dtype: int64
'''

print()

from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression()
modelo.fit(X_train, Y_train)

predicciones = modelo.predict(X_test)
print(predicciones)
'''
[0 0 1 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 1
 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 1 1 0 0 1 1 1 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0
 0 0 0 0 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 0 1 1 0 0
 0 1 1 0 1 0 0 0 0 1 0 1 0 1 1 1 1 0 0 1 1 1 1 0 0 1 0 1 1 0 1 0 1 0 1 1 1
 0 0 1 1 1 0 0 1 0 1 0 1 0 1 1 1 0 0 1 0 0 0 0 0 0 1 0 0 0 1 0 1 0 1 1 0 1
 0 1 0 1 0 0 1 0 1 1 1 0 1 1 0 0 0 0 1 0 0 0 0 0 1 1 1 0 0 0 0 0 0 1 0 1 0
 0 0 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 1 1 1 0 0 0 1 1
 0 0 0 1 0 0 0 0 0]
'''

print()

print(Y_test)
'''
248    1
197    0
133    1
169    0
736    0
      ..
422    0
815    0
466    0
559    1
6      0
Name: Survived, Length: 268, dtype: int64
'''

print()

from sklearn.metrics import classification_report

print(classification_report(Y_test, predicciones))
'''
              precision    recall  f1-score   support

           0       0.88      0.86      0.87       178
           1       0.73      0.77      0.75        90

    accuracy                           0.83       268
   macro avg       0.81      0.81      0.81       268
weighted avg       0.83      0.83      0.83       268
'''

print()

from sklearn.metrics import confusion_matrix

confusion_matrix(Y_test, predicciones)