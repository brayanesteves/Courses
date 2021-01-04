# Random Forest - Clasificación
print("Random Forest - Clasificación\n")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

vinos = pd.read_csv('vinos.csv')
vinos.head()

X = vinos.drop('Wine Type', axis=1)
y = vinos['Wine Type']

print(X)
'''
     Alcohol  Malic acid   Ash  Alcalinity of ash  ...  Color intensity   Hue  OD280/OD315 of diluted wines  Proline
0      14.23        1.71  2.43               15.6  ...             5.64  1.04                          3.92   1065.0
1      13.20        1.78  2.14               11.2  ...             4.38  1.05                          3.40   1050.0
2      13.16        2.36  2.67               18.6  ...             5.68  1.03                          3.17   1185.0
3      14.37        1.95  2.50               16.8  ...             7.80  0.86                          3.45   1480.0
4      13.24        2.59  2.87               21.0  ...             4.32  1.04                          2.93    735.0
..       ...         ...   ...                ...  ...              ...   ...                           ...      ...
173    13.71        5.65  2.45               20.5  ...             7.70  0.64                          1.74    740.0
174    13.40        3.91  2.48               23.0  ...             7.30  0.70                          1.56    750.0
175    13.27        4.28  2.26               20.0  ...            10.20  0.59                          1.56    835.0
176    13.17        2.59  2.37               20.0  ...             9.30  0.60                          1.62    840.0
177    14.13        4.10  2.74               24.5  ...             9.20  0.61                          1.60    560.0

[178 rows x 13 columns]
'''

print()

print(y)
'''
0        One
1        One
2        One
3        One
4        One
       ...
173    Three
174    Three
175    Three
176    Three
177    Three
Name: Wine Type, Length: 178, dtype: object
'''

print()

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3)

from sklearn.ensemble import RandomForestClassifier

randomforest = RandomForestClassifier(n_estimators=80)
randomforest.fit(X_train, Y_train)

predicciones = randomforest.predict(X_test)
print(predicciones)
'''
['Two' 'One' 'Three' 'One' 'One' 'Two' 'Two' 'Two' 'Three' 'Three' 'Three'
 'One' 'Two' 'One' 'Three' 'One' 'One' 'Three' 'One' 'Two' 'One' 'Two'
 'One' 'Two' 'Two' 'Two' 'One' 'One' 'Three' 'One' 'Two' 'One' 'Two' 'One'
 'One' 'Three' 'Three' 'One' 'Two' 'Two' 'Two' 'Three' 'Two' 'Two' 'One'
 'Two' 'One' 'Three' 'One' 'Two' 'Three' 'One' 'One' 'One']
'''

print()

print(Y_test)
'''
160    Three
140    Three
90       Two
0        One
33       One
17       One
158    Three
76       Two
41       One
99       Two
19       One
14       One
87       Two
105      Two
77       Two
163    Three
50       One
81       Two
37       One
113      Two
73       Two
70       Two
109      Two
102      Two
125      Two
10       One
36       One
123      Two
59       Two
11       One
173    Three
129      Two
95       Two
107      Two
29       One
42       One
58       One
82       Two
8        One
175    Three
103      Two
22       One
79       Two
157    Three
47       One
143    Three
166    Three
122      Two
69       Two
167    Three
26       One
142    Three
124      Two
32       One
Name: Wine Type, dtype: object
'''

print()

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(Y_test, predicciones))
'''
         One       1.00      1.00      1.00        17
       Three       0.93      1.00      0.97        14
         Two       1.00      0.96      0.98        23

    accuracy                           0.98        54
   macro avg       0.98      0.99      0.98        54
weighted avg       0.98      0.98      0.98        54
'''

print()

print(confusion_matrix(Y_test, predicciones))
'''
[[10  0  0]
 [ 0 16  0]
 [ 0  0 28]]
'''