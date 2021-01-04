# Máquinas de vector de soporte - Clasificación y regresión
print("Máquinas de vector de soporte - Clasificación y regresión\n")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

flores = sns.load_dataset('iris')
flores.head()

flores['species'].unique()

sns.pairplot(flores)
sns.pairplot(flores, hue='species')

from sklearn.model_selection import train_test_split

X = flores.drop('species', axis=1)
print(X)
'''
     sepal_length  sepal_width  petal_length  petal_width
0             5.1          3.5           1.4          0.2
1             4.9          3.0           1.4          0.2
2             4.7          3.2           1.3          0.2
3             4.6          3.1           1.5          0.2
4             5.0          3.6           1.4          0.2
..            ...          ...           ...          ...
145           6.7          3.0           5.2          2.3
146           6.3          2.5           5.0          1.9
147           6.5          3.0           5.2          2.0
148           6.2          3.4           5.4          2.3
149           5.9          3.0           5.1          1.8

[150 rows x 4 columns]
'''

print()

y = flores['species']
print(y)
'''
0         setosa
1         setosa
2         setosa
3         setosa
4         setosa
         ...
145    virginica
146    virginica
147    virginica
148    virginica
149    virginica
Name: species, Length: 150, dtype: object
'''

print()

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3)

print(X_train)
'''
     sepal_length  sepal_width  petal_length  petal_width
0             5.1          3.5           1.4          0.2
70            5.9          3.2           4.8          1.8
7             5.0          3.4           1.5          0.2
23            5.1          3.3           1.7          0.5
100           6.3          3.3           6.0          2.5
..            ...          ...           ...          ...
45            4.8          3.0           1.4          0.3
26            5.0          3.4           1.6          0.4
123           6.3          2.7           4.9          1.8
86            6.7          3.1           4.7          1.5
118           7.7          2.6           6.9          2.3

[105 rows x 4 columns]
'''

print()

print(X_test)
'''
     sepal_length  sepal_width  petal_length  petal_width
146           6.3          2.5           5.0          1.9
147           6.5          3.0           5.2          2.0
65            6.7          3.1           4.4          1.4
60            5.0          2.0           3.5          1.0
36            5.5          3.5           1.3          0.2
58            6.6          2.9           4.6          1.3
139           6.9          3.1           5.4          2.1
111           6.4          2.7           5.3          1.9
22            4.6          3.6           1.0          0.2
52            6.9          3.1           4.9          1.5
107           7.3          2.9           6.3          1.8
3             4.6          3.1           1.5          0.2
93            5.0          2.3           3.3          1.0
119           6.0          2.2           5.0          1.5
96            5.7          2.9           4.2          1.3
120           6.9          3.2           5.7          2.3
74            6.4          2.9           4.3          1.3
92            5.8          2.6           4.0          1.2
33            5.5          4.2           1.4          0.2
129           7.2          3.0           5.8          1.6
29            4.7          3.2           1.6          0.2
128           6.4          2.8           5.6          2.1
145           6.7          3.0           5.2          2.3
84            5.4          3.0           4.5          1.5
30            4.8          3.1           1.6          0.2
72            6.3          2.5           4.9          1.5
73            6.1          2.8           4.7          1.2
59            5.2          2.7           3.9          1.4
21            5.1          3.7           1.5          0.4
62            6.0          2.2           4.0          1.0
124           6.7          3.3           5.7          2.1
10            5.4          3.7           1.5          0.2
11            4.8          3.4           1.6          0.2
109           7.2          3.6           6.1          2.5
46            5.1          3.8           1.6          0.2
17            5.1          3.5           1.4          0.3
148           6.2          3.4           5.4          2.3
91            6.1          3.0           4.6          1.4
68            6.2          2.2           4.5          1.5
37            4.9          3.6           1.4          0.1
94            5.6          2.7           4.2          1.3
123           6.3          2.7           4.9          1.8
8             4.4          2.9           1.4          0.2
105           7.6          3.0           6.6          2.1
57            4.9          2.4           3.3          1.0
'''

print()

from sklearn.svm import SVC

modelo = SVC(gamma='auto')
modelo.fit(X_train, Y_train)

predicciones = modelo.predict(X_test)
print(predicciones)
'''
['setosa' 'versicolor' 'setosa' 'versicolor' 'setosa' 'setosa' 'virginica'
 'virginica' 'versicolor' 'virginica' 'versicolor' 'virginica' 'setosa'
 'versicolor' 'versicolor' 'virginica' 'versicolor' 'versicolor' 'setosa'
 'setosa' 'virginica' 'virginica' 'virginica' 'setosa' 'virginica'
 'versicolor' 'virginica' 'versicolor' 'virginica' 'setosa' 'setosa'
 'versicolor' 'virginica' 'versicolor' 'virginica' 'setosa' 'versicolor'
 'versicolor' 'setosa' 'setosa' 'setosa' 'setosa' 'versicolor'
 'versicolor' 'setosa']
'''

print()

print(Y_test)
'''
93     versicolor
63     versicolor
134     virginica
27         setosa
70     versicolor
52     versicolor
83     versicolor
26         setosa
142     virginica
118     virginica
73     versicolor
23         setosa
49         setosa
90     versicolor
88     versicolor
34         setosa
123     virginica
13         setosa
125     virginica
68     versicolor
128     virginica
35         setosa
3          setosa
108     virginica
54     versicolor
22         setosa
42         setosa
43         setosa
104     virginica
59     versicolor
77     versicolor
122     virginica
121     virginica
64     versicolor
96     versicolor
86     versicolor
39         setosa
66     versicolor
105     virginica
46         setosa
10         setosa
40         setosa
72     versicolor
131     virginica
126     virginica
Name: species, dtype: object
'''

print()

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(Y_test, predicciones))
'''
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        17
  versicolor       1.00      0.91      0.95        11
   virginica       0.94      1.00      0.97        17

    accuracy                           0.98        45
   macro avg       0.98      0.97      0.97        45
weighted avg       0.98      0.98      0.98        45
'''

print()

print(confusion_matrix(Y_test, predicciones))
'''
[[17  0  0]
 [ 0 15  0]
 [ 0  0 13]]
'''