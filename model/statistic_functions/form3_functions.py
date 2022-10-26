import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)

    return dataframe


def get_sales():
    df = get_data()
    sales = df["Sales"].sum()
    return int(sales)


def get_products():
    dataframe = get_data()
    all_products = dataframe["Product Name"].drop_duplicates()
    return all_products


def get_category():
    dataframe = get_data()
    category = dataframe["Category"].drop_duplicates()
    return category


def new_sales(product_name):
    print(product_name)
    df = get_data()
    print(df["Sales"].sum())
    total_sum = df[df["Product Name"] != product_name].sum()
    print(total_sum["Sales"])
    return int(total_sum["Sales"])


def scoatere_categorie(categorie_var):
    df = get_data()

    # Selectare coloane Category Sales Order Date
    category_df = df[["Category", "Sales", "Order Date"]]

    # Se scoate o categorie din lista de categorii
    uq_category = category_df[category_df["Category"] != str(categorie_var)]
    #dt.year ->
    df2 = uq_category.groupby(uq_category["Order Date"].dt.year).agg(['sum', 'max'])
    total_sum = uq_category["Sales"].sum()
    date = df2.index
    sum = df2["Sales"]["sum"].tolist()
    max = df2["Sales"]["max"].tolist()

    obj = [date, sum, max, int(total_sum)]
    return obj


def scoatere_produs(product_name):
    df = get_data()
    produse1 = df[["Order Date", "Sales", "Product Name", "Category"]]
    uq_produs = produse1[produse1["Product Name"] != str(product_name)]
    df2 = uq_produs.groupby(uq_produs["Order Date"].dt.year).agg(['sum', 'max'])

    total_sum = new_sales(product_name)

    date = df2.index
    sum = df2["Sales"]["sum"].tolist()
    max = df2["Sales"]["max"].tolist()

    obj = [date, sum, max, total_sum]
    return obj
