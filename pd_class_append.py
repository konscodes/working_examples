import pandas as pd

df_trades = pd.DataFrame(columns=['Symb', 'Position'])
symbol = 'ABC'
shares = 10
trade_data = {'Symb': symbol, 'Position': shares}
df_trades = df_trades.append(trade_data, ignore_index=True)
print(df_trades)

# Create a class for trades with methods add, update

class Trade:
    def __init__(self):
        self.dataframe = pd.DataFrame(columns=['Symb', 'Position'])

    def add(self, symbol, shares):
        trade_data = {'Symb': symbol, 'Position': shares}
        self.dataframe = self.dataframe.append(trade_data, ignore_index=True)
    
    def data(self):
        print(self.dataframe)

trade = Trade()
trade.add('AMD', 5)
trade.data()
trade.add('MU', 5)
trade.data()