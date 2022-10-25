import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)

    return dataframe


def total_sales_by_subCategory():
    dataframe = get_data()
    df = dataframe[["Sub-Category", "Sales", "Profit"]]
    df2 = df.groupby("Sub-Category").sum()

    index = df2.index
    sales = df2["Sales"]
    profit = df2["Profit"]
    # plt.barh(index,sales)
    # plt.barh(index,profit)
    # plt.show()
    obj = [index,sales,profit]
    return obj




def distributia_sub_categoiilor():
    dataframe = get_data()
    df = dataframe[["Category", "Sub-Category", "Sales"]]

    sub_category_list = df.drop_duplicates(subset="Sub-Category")["Sub-Category"]
    df_gp = df.groupby(["Category", "Sub-Category"]).size().unstack(fill_value=0)
    print(df_gp)
    index = df_gp.index

    # # x = df_gp["Accessories"]
    # for item in x:
    #     plt.bar(y,df_gp[f"{item}"])
    obj = [index, sub_category_list, df_gp]
    return obj


def frecventa_categoriilor():
    dataframe = get_data()
    df = dataframe[["Category", "Sub-Category", "Profit", "Row ID"]]
    df_gp = df.groupby(["Sub-Category", "Category"]).size().unstack(fill_value=0)
    print(df_gp)

    y = df_gp.index
    x = df_gp["Furniture"]
    x1 = df_gp["Office Supplies"]
    x2 = df_gp["Technology"]

    # plt.bar(y,x, )
    # plt.bar(y,x1)
    # plt.bar(y,x2)
    # plt.xticks(rotation=90)
    # plt.legend(["Furniture", "Office Supplies", "Technology"])
    # plt.tight_layout()

    # plt.show()
    obj = [y, x, x1, x2]
    return obj
