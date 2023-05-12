
import pandas as pd

data = pd.read_csv("./data/data.csv", encoding='gbk')
hang_val = data.iloc[1,:]

a = hang_val.tolist()
print(a)