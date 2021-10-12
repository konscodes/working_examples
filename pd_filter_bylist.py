import pandas as pd
import string
import random

random.seed(42)

df = pd.DataFrame({'col1': list(string.ascii_lowercase)[:11],
                   'col2':[random.randint(1,100) for x in range(11)]})

'''
Filter the items based on the list of column values for ex. ['a','c','h']
   col1 col2
0   a   64
1   b   3
2   c   28
3   d   23
4   e   74
5   f   68
6   g   90
7   h   9
8   i   43
9   j   3
10  k   22
'''

filtered_bool_series = df['col1'].isin(['a', 'c', 'h'])
selection = df[filtered_bool_series]
print(selection)

