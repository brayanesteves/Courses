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

sns.heatmap(casas.corr())
sns.heatmap(casas.corr(), annot=True)