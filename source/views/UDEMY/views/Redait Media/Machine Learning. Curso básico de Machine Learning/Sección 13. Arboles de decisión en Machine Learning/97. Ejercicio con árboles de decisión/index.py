'''
Data
https://www.mldata.io
'''

# Árboles de decisión - clasificación
print("Árboles de decisión - clasificación\n")

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

vinos = pd.read_csv('vinos.csv')
vinos.head()

vinos['Wine Type'].unique()
vinos['Wine Type'].value_counts()

X = vinos.drop('Wine Type', axis=1)
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

y = vinos['Wine Type']
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
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=45)

print(X_train)
'''
     Alcohol  Malic acid   Ash  Alcalinity of ash  ...  Color intensity   Hue  OD280/OD315 of diluted wines  Proline
97     12.29        1.41  1.98               16.0  ...             2.90  1.23                          2.74    428.0
172    14.16        2.51  2.48               20.0  ...             9.70  0.62                          1.71    660.0
30     13.73        1.50  2.70               22.5  ...             5.70  1.19                          2.71   1285.0
33     13.76        1.53  2.70               19.5  ...             5.40  1.25                          3.00   1235.0
80     12.00        0.92  2.00               19.0  ...             2.50  1.38                          3.12    278.0
..       ...         ...   ...                ...  ...              ...   ...                           ...      ...
95     12.47        1.52  2.20               19.0  ...             2.60  1.16                          2.63    937.0
32     13.68        1.83  2.36               17.2  ...             3.84  1.23                          2.87    990.0
124    11.87        4.31  2.39               21.0  ...             2.80  0.75                          3.64    380.0
131    12.88        2.99  2.40               20.0  ...             5.40  0.74                          1.42    530.0
158    14.34        1.68  2.70               25.0  ...            13.00  0.57                          1.96    660.0

[124 rows x 13 columns]
'''

print()

print(X_test)
'''
     Alcohol  Malic acid   Ash  Alcalinity of ash  ...  Color intensity   Hue  OD280/OD315 of diluted wines  Proline
97     12.29        1.41  1.98               16.0  ...             2.90  1.23                          2.74    428.0
172    14.16        2.51  2.48               20.0  ...             9.70  0.62                          1.71    660.0
30     13.73        1.50  2.70               22.5  ...             5.70  1.19                          2.71   1285.0
33     13.76        1.53  2.70               19.5  ...             5.40  1.25                          3.00   1235.0
80     12.00        0.92  2.00               19.0  ...             2.50  1.38                          3.12    278.0
..       ...         ...   ...                ...  ...              ...   ...                           ...      ...
95     12.47        1.52  2.20               19.0  ...             2.60  1.16                          2.63    937.0
32     13.68        1.83  2.36               17.2  ...             3.84  1.23                          2.87    990.0
124    11.87        4.31  2.39               21.0  ...             2.80  0.75                          3.64    380.0
131    12.88        2.99  2.40               20.0  ...             5.40  0.74                          1.42    530.0
158    14.34        1.68  2.70               25.0  ...            13.00  0.57                          1.96    660.0

[124 rows x 13 columns]

     Alcohol  Malic acid   Ash  Alcalinity of ash  ...  Color intensity   Hue  OD280/OD315 of diluted wines  Proline
153    13.23        3.30  2.28               18.5  ...            10.52  0.56                          1.51    675.0
161    13.69        3.26  2.54               20.0  ...             5.88  0.96                          1.82    680.0
0      14.23        1.71  2.43               15.6  ...             5.64  1.04                          3.92   1065.0
64     12.17        1.45  2.53               19.0  ...             2.95  1.45                          2.23    355.0
62     13.67        1.25  1.92               18.0  ...             3.80  1.23                          2.46    630.0
69     12.21        1.19  1.75               16.8  ...             2.85  1.28                          3.07    718.0
177    14.13        4.10  2.74               24.5  ...             9.20  0.61                          1.60    560.0
3      14.37        1.95  2.50               16.8  ...             7.80  0.86                          3.45   1480.0
10     14.10        2.16  2.30               18.0  ...             5.75  1.25                          3.17   1510.0
82     12.08        1.13  2.51               24.0  ...             2.20  1.31                          2.72    630.0
113    11.41        0.74  2.50               21.0  ...             3.08  1.10                          2.31    434.0
35     13.48        1.81  2.41               20.5  ...             5.10  1.04                          3.47    920.0
38     13.07        1.50  2.10               15.5  ...             3.70  1.18                          2.69   1020.0
160    12.36        3.83  2.38               21.0  ...             7.65  0.56                          1.58    520.0
91     12.00        1.51  2.42               22.0  ...             3.60  1.05                          2.65    450.0
90     12.08        1.83  2.32               18.5  ...             2.40  1.08                          2.27    480.0
99     12.29        3.17  2.21               18.0  ...             2.30  1.42                          2.83    406.0
61     12.64        1.36  2.02               16.8  ...             5.75  0.98                          1.59    450.0
149    13.08        3.90  2.36               21.5  ...             9.40  0.57                          1.33    550.0
165    13.73        4.36  2.26               22.5  ...             6.62  0.78                          1.75    520.0
109    11.61        1.35  2.70               20.0  ...             2.65  0.96                          3.26    680.0
150    13.50        3.12  2.62               24.0  ...             8.60  0.59                          1.30    500.0
29     14.02        1.68  2.21               16.0  ...             4.70  1.04                          3.59   1035.0
134    12.51        1.24  2.25               17.5  ...             5.45  0.75                          1.51    650.0
151    12.79        2.67  2.48               22.0  ...            10.80  0.48                          1.47    480.0
157    12.45        3.03  2.64               27.0  ...             7.50  0.67                          1.73    880.0
28     13.87        1.90  2.80               19.4  ...             4.50  1.25                          3.40    915.0
76     13.03        0.90  1.71               16.0  ...             4.60  1.19                          2.48    392.0
167    12.82        3.37  2.30               19.5  ...            10.26  0.72                          1.75    685.0
154    12.58        1.29  2.10               20.0  ...             7.60  0.58                          1.55    640.0
155    13.17        5.19  2.32               22.0  ...             7.90  0.60                          1.48    725.0
168    13.58        2.58  2.69               24.5  ...             8.66  0.74                          1.80    750.0
166    13.45        3.70  2.60               23.0  ...            10.68  0.85                          1.56    695.0
58     13.72        1.43  2.50               16.7  ...             6.80  0.89                          2.87   1285.0
117    12.42        1.61  2.19               22.5  ...             2.06  1.06                          2.96    345.0
144    12.25        3.88  2.20               18.5  ...             8.21  0.65                          2.00    855.0
34     13.51        1.80  2.65               19.0  ...             4.20  1.10                          2.87   1095.0
40     13.56        1.71  2.31               16.2  ...             6.13  0.95                          3.38    795.0
4      13.24        2.59  2.87               21.0  ...             4.32  1.04                          2.93    735.0
45     14.21        4.04  2.44               18.9  ...             5.24  0.87                          3.33   1080.0
112    11.76        2.68  2.92               20.0  ...             3.80  1.23                          2.50    607.0
127    11.79        2.13  2.78               28.5  ...             3.00  0.97                          2.44    466.0
89     12.08        1.33  2.30               23.6  ...             1.74  1.07                          3.21    625.0
119    12.00        3.43  2.00               19.0  ...             1.28  0.93                          3.05    564.0
85     12.67        0.98  2.24               18.0  ...             2.62  1.23                          3.16    450.0
156    13.84        4.12  2.38               19.5  ...             9.01  0.57                          1.64    480.0
162    12.85        3.27  2.58               22.0  ...             5.58  0.87                          2.11    570.0
132    12.81        2.31  2.40               24.0  ...             5.70  0.66                          1.36    560.0
25     13.05        2.05  3.22               25.0  ...             3.58  1.13                          3.20    830.0
66     13.11        1.01  1.70               15.0  ...             5.30  1.12                          3.18    502.0
13     14.75        1.73  2.39               11.4  ...             5.40  1.25                          2.73   1150.0
26     13.39        1.77  2.62               16.1  ...             4.80  0.92                          3.22   1195.0
159    13.48        1.67  2.64               22.5  ...            11.75  0.57                          1.78    620.0
44     13.05        1.77  2.10               17.0  ...             5.04  0.88                          3.35    885.0

[54 rows x 13 columns]
'''

print()

print(Y_train)
'''
97       Two
172    Three
30       One
33       One
80       Two
       ...
95       Two
32       One
124      Two
131    Three
158    Three
Name: Wine Type, Length: 124, dtype: object
'''

print()

print(Y_test)
'''
153    Three
161    Three
0        One
64       Two
62       Two
69       Two
177    Three
3        One
10       One
82       Two
113      Two
35       One
38       One
160    Three
91       Two
90       Two
99       Two
61       Two
149    Three
165    Three
109      Two
150    Three
29       One
134    Three
151    Three
157    Three
28       One
76       Two
167    Three
154    Three
155    Three
168    Three
166    Three
58       One
117      Two
144    Three
34       One
40       One
4        One
45       One
112      Two
127      Two
89       Two
119      Two
85       Two
156    Three
162    Three
132    Three
25       One
66       Two
13       One
26       One
159    Three
44       One
Name: Wine Type, dtype: object
'''

print()

from sklearn.tree import DecisionTreeClassifier

arbol = DecisionTreeClassifier()
arbol.fit(X_train, Y_train)

predicciones = arbol.predict(X_test)
print(predicciones)
'''
['Three' 'Three' 'One' 'Two' 'Two' 'Two' 'Three' 'One' 'One' 'Two' 'Two'
 'One' 'One' 'Three' 'Three' 'Two' 'Two' 'Three' 'Three' 'Three' 'Two'
 'Two' 'One' 'Three' 'Three' 'Three' 'One' 'Two' 'Three' 'Three' 'Three'
 'Three' 'Three' 'One' 'Two' 'Three' 'One' 'One' 'Two' 'One' 'Two' 'Two'
 'Two' 'Two' 'Two' 'Three' 'Three' 'Three' 'One' 'Two' 'One' 'One' 'Three'
 'One']
'''

print()

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(Y_test, predicciones))
'''
              precision    recall  f1-score   support

         One       1.00      0.94      0.97        16
       Three       0.90      0.95      0.93        20
         Two       0.89      0.89      0.89        18

    accuracy                           0.93        54
   macro avg       0.93      0.93      0.93        54
weighted avg       0.93      0.93      0.93        54
'''

print()

print(confusion_matrix(Y_test, predicciones))
'''
[[15  0  1]
 [ 0 19  1]
 [ 0  2 16]]
'''