import pandas as pd

df = pd.DataFrame()
print(df)

open_trades = pd.DataFrame(columns=['Symb', 'Position', 'Side', 'Status', 'Trade ID'])
trade_id = 1001
open_trades = open_trades.append({'Symb': 'ABC', 'Status': 'Open', 'Trade ID': 1002}, ignore_index=True)
open_trades = open_trades.append({'Symb': 'SEED', 'Status': 'Open', 'Trade ID': trade_id}, ignore_index=True)
condition = open_trades['Trade ID'] == trade_id
trade_index = open_trades.index[condition]
print(trade_index)
open_trades.at[trade_index, 'Position'] = 10
print(open_trades)