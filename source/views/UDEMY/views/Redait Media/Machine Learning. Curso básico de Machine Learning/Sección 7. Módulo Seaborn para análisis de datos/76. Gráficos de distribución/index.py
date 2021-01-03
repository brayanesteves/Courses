# Seaborn
print("Seaborn\n")

import seaborn as sns

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

sns.displot(propinas['total_bill'])
sns.displot(propinas['total_bill'], bins=30)
sns.displot(propinas['total_bill'], bins=20)
sns.displot(propinas['tips'], bins=20)
sns.displot(propinas['tips'], bins=10)

sns.jointplot(x='total_bill', y='tip', data=propinas)
# Hexagonal
sns.jointplot(x='total_bill', y='tip', data=propinas, kind='hex')
# Regresión lineal
sns.jointplot(x='total_bill', y='tip', data=propinas, kind='reg')
# Densidad
sns.jointplot(x='total_bill', y='tip', data=propinas, kind='kde')

sns.pairtplot(propinas)
sns.pairtplot(propinas, hue='sex')
sns.pairtplot(propinas, hue='size')

sns.rugplot(propinas['total_bill'])
sns.rugplot(propinas['tip'])
sns.rugplot(propinas['size'])