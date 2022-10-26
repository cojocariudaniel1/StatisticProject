import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot

def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    return dataframe

    # Evidenta celui mai prost cumparat produs dintr-o subcategorie comparativ cu categoria sa si cu totalul de categorii
    # Evidenta celui mai prost produs cumparat


def get_subcategory():
    df = get_data()
    return df["Sub-Category"].drop_duplicates().tolist()


#Evidenta celui mai prost produs cumparat
def evcmppc(subcategory):
    df = get_data()
    dataframe = df[["Product ID", "Sales", "Category", "Sub-Category"]]
    sub_category = dataframe[dataframe["Sub-Category"] == subcategory]
    result = sub_category.groupby("Product ID").mean(numeric_only=True).\
        sort_values(by="Sales", ascending=True).head(60)

    values = []

    for k in result.values:
        values.append(k[0])

    index = result.index
    obj = [index, values]
    return obj
