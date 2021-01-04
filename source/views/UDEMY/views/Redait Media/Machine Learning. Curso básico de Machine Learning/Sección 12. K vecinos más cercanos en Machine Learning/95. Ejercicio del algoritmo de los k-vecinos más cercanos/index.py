'''
Data .csv
https://www.mldata.io
'''

# K vecinos más cercanos
print("K vecinos más cercanos\n")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv('vehiculos.csv')
dataframe.head()

dataframe['vehicle_class'].unique()

y = dataframe['vehicle_class']
X = dataframe.drop('vehicle_class', axis=1)
print(X)
'''
     compactness  circularity  distance_circularity  ...  kurtosis_minor_axis  kurtosis_major_axis  hollows_ratio
0           95.0         48.0                  83.0  ...                 16.0                187.0          197.0
1           91.0         41.0                  84.0  ...                 14.0                189.0          199.0
2          104.0         50.0                 106.0  ...                  9.0                188.0          196.0
3           93.0         41.0                  82.0  ...                 10.0                199.0          207.0
4           85.0         44.0                  70.0  ...                 11.0                180.0          183.0
..           ...          ...                   ...  ...                  ...                  ...            ...
841         93.0         39.0                  87.0  ...                 25.0                188.0          195.0
842         89.0         46.0                  84.0  ...                 20.0                186.0          197.0
843        106.0         54.0                 101.0  ...                  4.0                187.0          201.0
844         86.0         36.0                  78.0  ...                 25.0                190.0          195.0
845         85.0         36.0                  66.0  ...                 18.0                186.0          190.0

[846 rows x 18 columns]
'''

print()

print(y)
'''
0       van
1       van
2      saab
3       van
4       bus
       ...
841    saab
842     van
843    saab
844    saab
845     van
Name: vehicle_class, Length: 846, dtype: object
'''

print()

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=45)

print(X_train)
'''
     compactness  circularity  distance_circularity  ...  kurtosis_minor_axis  kurtosis_major_axis  hollows_ratio
794         87.0         41.0                  76.0  ...                 13.0                188.0          195.0
317         95.0         45.0                 105.0  ...                 32.0                198.0          211.0
570        105.0         53.0                 108.0  ...                 35.0                189.0          203.0
750         96.0         40.0                  78.0  ...                 29.0                191.0          200.0
374         87.0         36.0                  53.0  ...                 15.0                180.0          183.0
..           ...          ...                   ...  ...                  ...                  ...            ...
725         91.0         37.0                  76.0  ...                 12.0                191.0          192.0
607         86.0         39.0                  62.0  ...                  9.0                199.0          204.0
544         88.0         43.0                  70.0  ...                  9.0                186.0          189.0
643         95.0         43.0                  83.0  ...                  4.0                196.0          198.0
414         85.0         45.0                  82.0  ...                 21.0                183.0          193.0

[592 rows x 18 columns]
'''

print()

print(X_test)
'''
     compactness  circularity  distance_circularity  ...  kurtosis_minor_axis  kurtosis_major_axis  hollows_ratio
547         88.0         44.0                  70.0  ...                  8.0                196.0          203.0
694        100.0         43.0                  92.0  ...                  9.0                195.0          205.0
559        101.0         56.0                 101.0  ...                  6.0                187.0          197.0
248        103.0         55.0                 103.0  ...                 16.0                188.0          196.0
720         91.0         38.0                  76.0  ...                 28.0                189.0          198.0
..           ...          ...                   ...  ...                  ...                  ...            ...
481        104.0         54.0                  91.0  ...                 21.0                187.0          196.0
436         93.0         42.0                  64.0  ...                 12.0                185.0          185.0
735         86.0         37.0                  77.0  ...                 13.0                186.0          191.0
63          83.0         42.0                  66.0  ...                  2.0                182.0          188.0
216         84.0         44.0                  77.0  ...                  2.0                183.0          187.0

[254 rows x 18 columns]
'''

print()

print(Y_train)
'''
794     bus
317    saab
570    saab
750    saab
374     van
       ...
725     van
607     van
544     bus
643     bus
414     van
Name: vehicle_class, Length: 592, dtype: object
'''

print()

print(Y_test)
'''
547     bus
694    saab
559    saab
248    opel
720    opel
       ...
481    opel
436     van
735    opel
63      bus
216    saab
Name: vehicle_class, Length: 254, dtype: object
'''

print()

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, Y_train)

predicciones = knn.predict(X_test)
print(predicciones)
'''
['saab' 'opel' 'saab' 'opel' 'saab' 'van' 'saab' 'opel' 'saab' 'van'
 'opel' 'bus' 'van' 'opel' 'opel' 'van' 'opel' 'saab' 'bus' 'saab' 'bus'
 'bus' 'bus' 'bus' 'bus' 'bus' 'opel' 'saab' 'van' 'bus' 'opel' 'opel'
 'bus' 'saab' 'opel' 'bus' 'van' 'bus' 'bus' 'van' 'van' 'opel' 'opel'
 'bus' 'saab' 'van' 'bus' 'bus' 'opel' 'bus' 'bus' 'saab' 'opel' 'van'
 'bus' 'saab' 'saab' 'bus' 'saab' 'opel' 'van' 'van' 'bus' 'bus' 'saab'
 'van' 'bus' 'bus' 'van' 'saab' 'van' 'bus' 'opel' 'van' 'opel' 'van'
 'saab' 'saab' 'bus' 'bus' 'van' 'saab' 'saab' 'van' 'bus' 'bus' 'saab'
 'saab' 'saab' 'van' 'van' 'van' 'van' 'saab' 'saab' 'saab' 'saab' 'opel'
 'opel' 'saab' 'bus' 'bus' 'bus' 'saab' 'van' 'bus' 'saab' 'saab' 'saab'
 'bus' 'van' 'bus' 'opel' 'bus' 'saab' 'saab' 'opel' 'van' 'opel' 'opel'
 'bus' 'opel' 'bus' 'van' 'saab' 'opel' 'saab' 'opel' 'opel' 'bus' 'bus'
 'bus' 'van' 'opel' 'van' 'bus' 'bus' 'opel' 'opel' 'saab' 'van' 'opel'
 'van' 'van' 'saab' 'bus' 'saab' 'saab' 'bus' 'van' 'van' 'bus' 'saab'
 'saab' 'van' 'van' 'van' 'bus' 'opel' 'bus' 'saab' 'saab' 'opel' 'saab'
 'van' 'saab' 'van' 'van' 'bus' 'van' 'saab' 'opel' 'van' 'van' 'van'
 'saab' 'van' 'van' 'bus' 'bus' 'opel' 'van' 'van' 'opel' 'saab' 'opel'
 'opel' 'opel' 'van' 'van' 'opel' 'bus' 'opel' 'saab' 'bus' 'bus' 'opel'
 'bus' 'bus' 'bus' 'van' 'van' 'bus' 'bus' 'bus' 'opel' 'opel' 'van' 'van'
 'bus' 'bus' 'bus' 'van' 'van' 'van' 'opel' 'van' 'bus' 'saab' 'van' 'van'
 'bus' 'bus' 'saab' 'van' 'bus' 'van' 'bus' 'bus' 'saab' 'saab' 'bus'
 'saab' 'bus' 'bus' 'saab' 'saab' 'bus' 'bus' 'van' 'bus' 'bus' 'saab'
 'saab' 'saab' 'opel' 'bus' 'van' 'opel' 'opel' 'van' 'opel' 'bus' 'bus']
'''

print()

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(Y_test, predicciones))
'''
[[65  0  7  5]
 [ 7 24 28  6]
 [ 5 26 23  3]
 [ 2  0  2 51]]
'''

print()

print(classification_report(Y_test, predicciones))
'''
              precision    recall  f1-score   support

         bus       0.82      0.84      0.83        77
        opel       0.48      0.37      0.42        65
        saab       0.38      0.40      0.39        57
         van       0.78      0.93      0.85        55

    accuracy                           0.64       254
   macro avg       0.62      0.64      0.62       254
weighted avg       0.63      0.64      0.63       254
'''

print()

tasa_error = []
for i in range(1, 30):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, Y_train)
    prediccion_i = knn.predict(X_test)
    tasa_error.append(np.mean(prediccion_i != Y_test))

print(tasa_error)
'''
[0.35826771653543305, 0.3464566929133858, 0.3188976377952756, 0.3228346456692913, 0.33858267716535434, 0.3346456692913386, 0.3228346456692913, 0.33858267716535434, 0.36220472440944884, 0.3661417322834646, 0.35039370078740156, 0.3661417322834646, 0.36220472440944884, 0.38188976377952755, 0.35039370078740156, 0.3661417322834646, 0.3661417322834646, 0.3700787401574803, 0.3661417322834646, 0.3779527559055118, 0.3661417322834646, 0.37401574803149606, 0.37401574803149606, 0.37401574803149606, 0.3779527559055118, 0.38976377952755903, 0.38188976377952755, 0.3700787401574803, 0.37401574803149606]
'''

print()

valores = range(1, 30)
plt.plot(valores, tasa_error, color='green', marker='o', markerfacecolor='red', markersize=8)
plt.show()

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)
predicciones = knn.predict(X_test)
print(classification_report(Y_test, predicciones))
'''
              precision    recall  f1-score   support

         bus       0.77      0.88      0.82        77
        opel       0.58      0.45      0.50        65
        saab       0.44      0.39      0.41        57
         van       0.82      0.98      0.89        55

    accuracy                           0.68       254
   macro avg       0.65      0.67      0.66       254
weighted avg       0.66      0.68      0.66       254
'''