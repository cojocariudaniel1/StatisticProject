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

def get_products():
    dataframe = get_data()
    all_products = dataframe["Product Name"].drop_duplicates()
    return all_products




def evolutia_dis_vanz(product_name):
    df = get_data()
    product = df[["Product Name", "Discount", "Sales", "Profit"]].sort_values(ascending=False, by="Discount")
    uq_product = product[product["Product Name"] == str(product_name)]
    print(uq_product)
    # uq_product.plot()

    plt.plot(uq_product["Discount"],uq_product["Sales"])
    plt.plot(uq_product["Discount"],uq_product["Profit"])
    plt.plot(uq_product["Discount"],uq_product["Discount"])

    discount = uq_product["Discount"].tolist()
    sales = uq_product["Sales"].tolist()
    profit = uq_product["Profit"].tolist()

    obj = [discount,sales,profit]
    return obj
    # plt.legend(["Sales", "Profit","Discount"])
    # plt.xlabel("Discount")
    # plt.ylabel("Sales")

    # plt.plot(uq_product["Sales"],uq_product["Sales"])
    # plt.bar(uq_product["Discount"],uq_product["Sales"])
    # plt.tight_layout()
    # plt.show()



