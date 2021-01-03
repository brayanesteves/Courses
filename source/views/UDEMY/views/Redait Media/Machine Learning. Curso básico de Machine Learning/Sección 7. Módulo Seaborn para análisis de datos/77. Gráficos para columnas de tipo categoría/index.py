# Gráficos para categorías
print("Gráficos para categorías\n")

import seaborn as sns
import numpy as np

propinas = sns.load_dataset('tips')
propinas.head(10)
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
5       25.29  4.71    Male     No  Sun  Dinner     4
6        8.77  2.00    Male     No  Sun  Dinner     2
7       26.88  3.12    Male     No  Sun  Dinner     4
8       15.04  1.96    Male     No  Sun  Dinner     2
9       14.78  3.23    Male     No  Sun  Dinner     2
'''

sns.barplot(x='sex', y='total_bill', data=propinas)

sns.countplot(x='sex', data=propinas)
sns.countplot(x='smoker', data=propinas)

sns.boxplot(x='day', y='total_bill', data=propinas)
sns.boxplot(x='day', y='total_bill', data=propinas, hue='smoker')

sns.violinplot(x='day', y='total_bill', data=propinas)
sns.violinplot(x='day', y='total_bill', data=propinas, hue='smoker')
sns.violinplot(x='day', y='total_bill', data=propinas, hue='smoker', split=True)

sns.stripplot(x='day', y='total_bill', data=propinas)
sns.stripplot(x='day', y='total_bill', data=propinas, hue='sex')

sns.swarmplot(x='day', y='total_bill', data=propinas, hue='sex')

sns.violinplot(x='day', y='total_bill', data=propinas)
sns.swarmplot(x='day', y='total_bill', data=propinas)