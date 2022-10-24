import random

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_name = "Superbaza.xls"  # path to file + file name
sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

dataframe = pd.DataFrame(df)


# dataframe.filter("Product ID")
# print(dataframe)
def test():
    data = dataframe
    # print(data)
    data_max = data.sort_values(ascending=False, by="Profit").iloc[:5]
    data_min = data.sort_values(ascending=True, by="Profit").iloc[:5]
    mean = data["Profit"].mean()
    # print(mean)
    # print(data_max)
    # print(data_min)

    ts = data_max[["Order Date", "Profit"]]
    ts.plot(y="Order Date", x="Profit")
    print(ts)
    plt.show()




# test()
def test2():
    data = dataframe
    x = data.loc[data['Product ID'] == data["Product ID"].iloc[random.randint(1, len(data))]]

    temp = x
    print(temp)
    order_date_data = temp["Order Date"].sort_values(ascending=True).tolist()
    profit_data = temp["Profit"].tolist()

    op = [order_date_data, profit_data]
    print(len(order_date_data))
    print(len(profit_data))
    return op


