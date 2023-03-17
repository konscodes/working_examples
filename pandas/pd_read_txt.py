import os
import io
import pandas as pd

with open('python-finance/trades/trade.txt', 'r') as f:
    data = f.read().replace('\n',';').replace(';;','\n')
    print(data)
    
df = pd.read_csv(io.StringIO(data), sep=";", header=None)
print(df)
df.to_csv('trade.csv')