import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot

x1 = "Newell 322"
x2 = "Riverside Palais Royal Lawyers Bookcase, Royale Cherry Finish"
x3 = "Aastra 57i VoIP phone"
x4 = "AT&T CL83451 4-Handset Telephone"


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
    print(len(obj[0]))
    return obj
evcmppc("Bookcases")