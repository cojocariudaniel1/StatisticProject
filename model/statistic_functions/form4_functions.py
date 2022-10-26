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
    all_products = dataframe["Product Name"].drop_duplicates()
    return all_products


def evolutia_dis_vanz(product_name):
    df = get_data()
    product = df[["Product Name", "Discount", "Sales", "Profit"]].sort_values(ascending=False, by="Discount")
    uq_product = product[product["Product Name"] == str(product_name)]

    # Se selecteaza cele 3 liste dupa ce au fost filtrate in baza de date in functie de numele la produs
    discount = uq_product["Discount"].tolist()
    sales = uq_product["Sales"].tolist()
    profit = uq_product["Profit"].tolist()

    obj = [discount, sales, profit]
    return obj
