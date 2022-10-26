import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    # DataFrame (Tabel de date coloane si linii (24 coloane, 10.000 linii)
    dataframe = pd.DataFrame(df)
    return dataframe


def get_products():
    dataframe = get_data()
    all_products = dataframe["Product Name"].drop_duplicates().tolist()
    return all_products


def perioada_de_timp(product_name):
    dataframe = get_data()

    try:
        # Se selecteaza coloana order date product name si profit din DataBase
        df = dataframe[["Order Date", "Product Name", "Profit"]]
        # Se filtreaza coloana product name in functie de product name si se ordoneaza.
        df2 = df[df["Product Name"] == product_name].sort_values(by="Order Date")

        order_date = df2["Order Date"].tolist()
        profit = df2["Profit"]
        obj = [order_date, profit]
        return obj

    except Exception as e:
        print(e)


def zona_de_distributie(product_name):
    dataframe = get_data()
    # Se selecteaza coloana State, Profit, Product Name
    df = dataframe[["State", "Profit", "Product Name"]]

    # Se filtreaza product name si se sorteaza datele
    df2 = df[df["Product Name"] == product_name].sort_values(by="State")
    region = df2["State"].tolist()  # Se atribui variabilei region toate statele
    profit = df2["Profit"].tolist()
    obj = [region, profit]
    return obj  # Se returneaza cele 2 liste (x, y)


def profilul_clientilor(product_name):
    dataframe = get_data()
    # Se aleg coloanele Segmentt Profit si Product Name
    df = dataframe[["Segment", "Profit", "Product Name"]]
    # Se filtreaza dupa product name
    df2 = df[df["Product Name"] == product_name]

    segment = df2["Segment"].tolist()
    profit = df2["Profit"].tolist()

    obj = [segment, profit]
    return obj
