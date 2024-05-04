# add your code here
import pandas as pd

df_fruit_sales = pd.Dataframe({"Apples": [35, 41], "Bananas": [21, 34]}, index = ["2017 Sales", "2018 Sales"])
print(df_fruit_sales)
df_fruit_sales.to_csv("fruit.csv")