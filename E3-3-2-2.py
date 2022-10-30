import pandas as pd
df1 = pd.read_csv('2017pig.csv',encoding="utf-8", sep=",")
df1.columns = [ 'total_amt', 'average_weight', 'average_price']
print(df1.describe())
print(df1.average_price.max())
print(df1.sort_values("average_price", ascending=False).head(5))
print(df1[df1.acerage_price>90])