import pandas as pd

data_dict = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
             'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(data_dict)

print(f"Column types:\n{df.dtypes}")

col_one_list = df['one'].tolist()
col_one_arr = df['one'].to_numpy()

print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")
print(f"\ncol_one_arr:\n{col_one_arr}\ntype:{type(col_one_arr)}")