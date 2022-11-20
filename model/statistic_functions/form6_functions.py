import pandas as pd


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    return dataframe


def top_5_produse_pe_subcategorie(subcategory):
    dataframe = get_data()
    # Se selecteaza coloanele Category, Sub-Category, Sales
    df = dataframe[["Product ID", "Sub-Category", "Profit"]]
    sub_category = df[df["Sub-Category"] == subcategory]
    result = sub_category.groupby("Product ID").sum(numeric_only=True). \
        sort_values(by="Profit", ascending=False).head(20)
    values = []

    for k in result.values:
        values.append(k[0])

    index = result.index
    obj = [index, values]
    return obj
