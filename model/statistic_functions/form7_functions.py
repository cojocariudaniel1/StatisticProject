import pandas as pd
from matplotlib import pyplot as plt


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    return dataframe


def profit_pe_an(categorie_var):
    df = get_data()
    # Se selecteaza coloanele Category, Sub-Category, Sales
    category_df = df[["Category", "Profit", "Order Date"]]

    uq_category = category_df[category_df["Category"] == str(categorie_var)]
    #dt.year ->
    df2 = uq_category.groupby(uq_category["Order Date"].dt.year).agg(['sum'],numeric_only=True)
    date = df2.index
    sum = df2["Profit"]["sum"].tolist()
    obj = [date, sum]
    return obj

