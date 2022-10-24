import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    return dataframe


def get_products():
    dataframe = get_data()
    all_products = dataframe["Product Name"].tolist()
    return all_products


def profilul_clientilor(product_name):
    print(product_name)
    dataframe = get_data()
    df = dataframe[["Segment", "Profit", "Product Name"]]
    df2 = df[df["Product Name"] == product_name]
    # x = df.filter(like="Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back", axis=0)

    segment = df2["Segment"].tolist()
    profit = df2["Profit"].tolist()
    print(df2)


    # obj.groupby(by="Segment").plot(kind="line")
    op = [segment, profit]
    return op
