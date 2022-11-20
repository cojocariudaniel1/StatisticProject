import pandas as pd
from matplotlib import pyplot as plt


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    return dataframe


def pondere_vanzari(sub_categorie):
    df = get_data()
    # Se selecteaza coloanele Category, Sub-Category, Sales

    df1 = df["Sub-Category"].drop_duplicates().values
    print(len(df1))

    category = df[df["Sub-Category"] == sub_categorie]
    total_vanzari = category["Sales"].sum()

    df1 = category.groupby(['Product Name'])
    sum_sales = df1[["Product Name", "Sales"]].agg('sum', numeric_only=True).reset_index()

    product_max_sales = sum_sales.sort_values(by="Sales", ascending=False).head(1)




    pondere_vanzari_produs = (product_max_sales["Sales"].values[0]/ total_vanzari) * 100
    print(f"Pondere vanzari: {pondere_vanzari_produs:.2f}%")
    x1 = pondere_vanzari_produs
    x2 = 100 - pondere_vanzari_produs
    labels = [product_max_sales["Product Name"].values[0], f"Total Vanzari: {sub_categorie}"]
    print(f"{x2:.2f}")
    explode = (0, 0.1)
    # plt.pie([x1,x2], explode=explode, labels=labels, autopct='%1.1f%%',
    #         shadow=True, startangle=90)
    # plt.show()
    obj = [x1,x2, labels, explode]
    return obj
    # # Total vanzari
    # Total vanzari produs selectat
    # Ponderea vanzarilor produsului in functie de vanzarile toale


if __name__ == "__main__":
    pondere_vanzari("Fasteners")
