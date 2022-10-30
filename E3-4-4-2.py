import json
import pandas as pd

with open("AQI.json", encoding = "utf8") as file:
    data = json.load(file)

df = pd.DataFrame(data)
print(df)
df1 = pd.sort_values(by="AQI", ascending=False)
print("以AQI遞減排序")
print(df1["AQI"])
print(df1.froupby("county").count()["SiteName"])
df2=df1["AQI"]
print(df2.describe())