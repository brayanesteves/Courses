# Regresión Lineal con Python
print("Regresión Lineal con Python\n")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

casas = pd.read_csv('USA_Housing.csv')
print(casas)
'''
      Avg. Area Income  Avg. Area House Age  ...         Price                                            Address
0         79545.458574             5.682861  ...  1.059034e+06  208 Michael Ferry Apt. 674\nLaurabury, NE 3701...
1         79248.642455             6.002900  ...  1.505891e+06  188 Johnson Views Suite 079\nLake Kathleen, CA...
2         61287.067179             5.865890  ...  1.058988e+06  9127 Elizabeth Stravenue\nDanieltown, WI 06482...
3         63345.240046             7.188236  ...  1.260617e+06                          USS Barnett\nFPO AP 44820
4         59982.197226             5.040555  ...  6.309435e+05                         USNS Raymond\nFPO AE 09386
...                ...                  ...  ...           ...                                                ...
4995      60567.944140             7.830362  ...  1.060194e+06                   USNS Williams\nFPO AP 30153-7653
4996      78491.275435             6.999135  ...  1.482618e+06              PSC 9258, Box 8489\nAPO AA 42991-3352
4997      63390.686886             7.250591  ...  1.030730e+06  4215 Tracy Garden Suite 076\nJoshualand, VA 01...
4998      68001.331235             5.534388  ...  1.198657e+06                          USS Wallace\nFPO AE 73316
4999      65510.581804             5.992305  ...  1.298950e+06  37778 George Ridges Apt. 509\nEast Holly, NV 2...

[5000 rows x 7 columns]
'''

casas.head(20)

casas.info()

casas.describe()

casas.columns

casas['Price']

sns.displot(casas['Price'])

print()

sns.heatmap(casas.corr())
sns.heatmap(casas.corr(), annot=True)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

casas.head()
casas.columns

X = casas[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
print(X)
'''
      Avg. Area Income  Avg. Area House Age  Avg. Area Number of Rooms  Avg. Area Number of Bedrooms  Area Population
0         79545.458574             5.682861                   7.009188                          4.09     23086.800503
1         79248.642455             6.002900                   6.730821                          3.09     40173.072174
2         61287.067179             5.865890                   8.512727                          5.13     36882.159400
3         63345.240046             7.188236                   5.586729                          3.26     34310.242831
4         59982.197226             5.040555                   7.839388                          4.23     26354.109472
...                ...                  ...                        ...                           ...              ...
4995      60567.944140             7.830362                   6.137356                          3.46     22837.361035
4996      78491.275435             6.999135                   6.576763                          4.02     25616.115489
4997      63390.686886             7.250591                   4.805081                          2.13     33266.145490
4998      68001.331235             5.534388                   7.130144                          5.44     42625.620156
4999      65510.581804             5.992305                   6.792336                          4.07     46501.283803

[5000 rows x 5 columns]
'''

print()

Y = casas['Price']
print(Y)
'''
0       1.059034e+06
1       1.505891e+06
2       1.058988e+06
3       1.260617e+06
4       6.309435e+05
            ...
4995    1.060194e+06
4996    1.482618e+06
4997    1.030730e+06
4998    1.198657e+06
4999    1.298950e+06
Name: Price, Length: 5000, dtype: float64
'''

# Datos de entrenamiento
# 0.3 = 30% (Datos de pruebas)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
print(X_train)
'''
      Avg. Area Income  Avg. Area House Age  Avg. Area Number of Rooms  Avg. Area Number of Bedrooms  Area Population
1840      55245.337288             3.965745                   8.961106                          4.38     43557.943435
2115      62305.638407             6.490769                   7.647362                          3.19     47066.617420
4437      77345.472379             5.407515                   8.243178                          3.11     26706.911029
1146      65846.171039             6.385374                   6.804131                          3.18     28214.363551
2486      69350.793357             6.910415                   8.288048                          4.29     36779.058567
...                ...                  ...                        ...                           ...              ...
4426      76223.561256             6.371627                   5.342217                          2.42     30165.337445
466       56685.014442             6.958045                   7.502115                          3.38     43322.166854
3092      66195.337714             6.507971                   6.611861                          3.14     37288.923574
3772      58694.515017             7.394768                   9.269453                          4.32     49960.977236
860       61162.580254             5.896316                   7.880521                          6.04     36033.701431

[3500 rows x 5 columns]
'''

print()

print(X_test)
'''
      Avg. Area Income  Avg. Area House Age  Avg. Area Number of Rooms  Avg. Area Number of Bedrooms  Area Population
1501      61907.593345             7.017838                   6.440256                          3.25     43828.947207
2586      57160.202243             6.893260                   6.921532                          3.13     43467.147035
2653      70190.796445             6.745054                   6.662567                          2.01     29215.136112
1055      69316.796889             6.300409                   7.873576                          4.28     24448.211461
705       72991.481649             3.412866                   6.494081                          2.48     50626.495426
...                ...                  ...                        ...                           ...              ...
3563      74208.124644             6.259782                   8.666717                          3.38     25507.336340
1538      71112.350296             5.612677                   7.419542                          4.26     24134.413996
1837      63665.394418             6.729105                   7.732959                          3.43     44029.681816
2380      56073.892443             6.576733                   6.959056                          4.40     64149.680213
1912      66774.181946             5.476416                   8.060545                          3.12     23793.337043

[1500 rows x 5 columns]
'''

print()

print(Y_train)
'''
1840    8.814461e+05
2115    1.375771e+06
4437    1.137069e+06
1146    9.289500e+05
2486    1.392084e+06
            ...
4426    1.023944e+06
466     1.223101e+06
3092    1.318598e+06
3772    1.708631e+06
860     1.060898e+06
Name: Price, Length: 3500, dtype: float64
'''

print()

print(Y_test)
'''
1501    1.339096e+06
2586    1.251794e+06
2653    1.340095e+06
1055    1.431508e+06
705     1.042374e+06
            ...
3563    1.348222e+06
1538    1.309937e+06
1837    1.472887e+06
2380    1.409762e+06
1912    1.009606e+06
Name: Price, Length: 1500, dtype: float64
'''

# Modelo de entrenamiento
print("\nModelo de entrenamiento\n")

lrm = LinearRegression()
lrm.fit(X_train, Y_train)

# Modelo de pruebas
print("\nModelo de pruebas\n")

from sklearn import metrics

predicciones = lrm.predict(X_test)
print(predicciones)

plt.scatter(Y_test, predicciones)
plt.show()

sns.displot(Y_test - predicciones)

'''
MAE (Mean absolute error) - Media del valor absoluto de los errores
'''
metrics.mean_absolute_error(Y_test, predicciones)

'''
MSE (Media de los errores al cuadrado)
'''
metrics.mean_squared_error(Y_test, predicciones)

'''
RMSE
'''
np.sqrt(metrics.mean_squared_error(Y_test, predicciones))