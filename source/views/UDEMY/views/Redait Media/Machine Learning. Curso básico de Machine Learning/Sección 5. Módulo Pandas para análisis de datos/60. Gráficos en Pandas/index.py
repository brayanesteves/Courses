import numpy as np
import pandas as pd

dataframe = pd.DataFrame(np.random.randint(200, size=(50, 4)), columns=['a', 'b', 'c', 'd'])
print(dataframe)
'''
      a    b    c    d
0   120  134   54  169
1   116   78  168  158
2   191   51   56   48
3    39  170  150  174
4   190  130  104   69
5   110   45   31   84
6   179   20   22  110
7   142  108   77   46
8    47   68    1  160
9   151   72   82   28
10   27   98   12   81
11   79   96   97   57
12   88  139  118  151
13   57   72  136  133
14  129   36   57   77
15   89   27  107   17
16  152   49    7  136
17  155  152  121  112
18   37  100  182  144
19  162   79   69   43
20   79   24   84   16
21   99   26  192   38
22  184  130   22  138
23  175   30  125   89
24  139  102   56  196
25  119  138  148  135
26  198  143   16  151
27  191  151   96  149
28  136   12   94   86
29   35   91  165  117
30   22    5  173   47
31  113  120   64  184
32  113  162   90    3
33    9   83  131   89
34   44  171   43   17
35   18  198  149   32
36  188  138   33   45
37   30  183   36    9
38   57   15  162   45
39   41  199  196   99
40   20   83  102  141
41   41   90   50   77
42   45  169  154  159
43   59   84   63  119
44   39   88   47  183
45   83  181   25   62
46  145   21   87   61
47   61  191  102  115
48   93   11   89  152
49   41  111   51  173
'''

print()

dataframe['a'].hist()

print()

dataframe['b'].hist()

print()

dataframe['b'].hist(bins=30)

print()

dataframe['a'].plot.hist()

print()

dataframe.plot.area()

print()

dataframe.plot.area(alpha=0.3)

print()

dataframe.plot.bar()

print()

dataframe.plot.bar(stacked=True)

print()

dataframe.plot.scatter(x='a', y='b')

print()

dataframe.plot.scatter(x='a', y='b', c='c', cmap='coolwarm')

print()

dataframe.plot.box()

print()

dataframe.plot.hexbin(x='a', y='b', gridsize=12)

print()

dataframe.plot.kde()

print()

dataframe.plot.density()