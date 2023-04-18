from vnstock import *
import pandas as pd

df = stock_historical_data("VNM", "2016-01-01", "2023-04-15")
df2 = dividend_history("VNM")
# print(df2)
d1 = price_board('TCB,SSI,VND')
# print(d1)
# pd.DataFrame(df).to_excel("stock.xlsx")
# pd.DataFrame(df2).to_excel("dvd.xlsx")
pd.DataFrame(d1).to_excel("d1.xlsx")
