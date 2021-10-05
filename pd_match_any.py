import pandas as pd

open_trades = pd.DataFrame(columns=['Symb', 'Position', 'Side', 'Status', 'Trade ID'])
trade_id = 1001
open_trades = open_trades.append({'Symb': 'ABC', 'Status': 'Closed', 'Trade ID': 1000}, ignore_index=True)
open_trades = open_trades.append({'Symb': 'ABC', 'Status': 'Open', 'Trade ID': 1002}, ignore_index=True)
open_trades = open_trades.append({'Symb': 'SEED', 'Status': 'Open', 'Trade ID': trade_id}, ignore_index=True)
print(open_trades)
print((open_trades['Symb'] == 'ABC').any())
symb = open_trades['Symb'] == 'ABC'
print(symb)
status = open_trades['Status'] == 'Open'
print(status)
match = open_trades[symb & status]
print(match)