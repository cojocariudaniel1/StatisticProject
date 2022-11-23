import os

import pandas as pd
import xlsxwriter


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


def export_scoatere_categorie(func, item, patch="data.xlsx"):
    if func == 0:
        obj = scoatere_categorie(item)
        date = obj[0]
        sum = obj[1]
        max = obj[2]
    else:
        obj = scoatere_produs(item)
        date = obj[0]
        sum = obj[1]
        max = obj[2]

    header = ["Date", "Sum", "Max"]
    workbook = xlsxwriter.Workbook(patch[0])
    worksheet = workbook.add_worksheet()
    worksheet.write_row('A1', header)
    worksheet.write_column('A2', date)
    worksheet.write_column('B2', sum)
    worksheet.write_column('C2', max)

    data_len = len(sum) + 1
    chart = workbook.add_chart({'type': 'column'})

    chart.add_series({
        'categories': f'=Sheet1!$A$2:$A${data_len}',
        'values': f'=Sheet1!$B$2:$B${data_len}',
        'name': '=Sheet1!$B$1'

    })
    chart.add_series({
        'categories': f'=Sheet1!$A$2:$A${data_len}',
        'values': f'=Sheet1!$C$2:$C${data_len}',
        'name': '=Sheet1!$C$1'

    })
    worksheet.conditional_format(f'B2:B{data_len}', {'type': '3_color_scale'})
    worksheet.conditional_format(f'C2:B{data_len}', {'type': '3_color_scale'})

    worksheet.insert_chart('E2', chart)
    workbook.close()
    full_path_to_file = str(patch[0])
    os.startfile(full_path_to_file)


def scoatere_categorie(categorie_var):
    df = get_data()

    # Selectare coloane Category Sales Order Date
    category_df = df[["Category", "Sales", "Order Date"]]

    # Se scoate o categorie din lista de categorii
    uq_category = category_df[category_df["Category"] != str(categorie_var)]
    # dt.year ->
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
