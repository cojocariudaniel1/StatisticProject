import logging
import os

import pandas as pd
import xlsxwriter


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)

    return dataframe

def export_frecventa_categoriilor(patch="data.xlsx"):
    try:
        df = frecventa_categoriilor()
        header = df[0]
        workbook = xlsxwriter.Workbook(patch[0])
        worksheet = workbook.add_worksheet()

        worksheet.write_row('A1', header)
        worksheet.write_row('A2', df[1])
        worksheet.write_row('A3', df[2])
        worksheet.write_row('A4', df[3])
        chart = workbook.add_chart({'type': 'bar'})

        chart.add_series({
            'categories': '=Sheet1!$A$1:$Q$1',
            'values': '=Sheet1!$A$2:$Q$2',
            'name': 'Furniture'

        })
        data_len = len(df[0]) + 1
        chart.add_series({
            'categories': '=Sheet1!$A$1:$Q$1',
            'values': '=Sheet1!$A$3:$Q$3',
            'name': 'Office Supplies'

        })

        chart.add_series({
            'categories': '=Sheet1!$A$1:$Q$1',
            'values': '=Sheet1!$A$4:$Q$4',
            'name': 'Tehnology'

        })

        worksheet.insert_chart('D2', chart)
        # worksheet.conditional_format(f'B2:B{data_len}', {'type': '3_color_scale'})
        # worksheet.conditional_format(f'C2:C{data_len}', {'type': '3_color_scale'})

        workbook.close()
        full_path_to_file = str(patch[0])
        os.startfile(full_path_to_file)
    except BaseException as e:
        logging.exception(e)


def export_distributia_categoriilor(patch="data.xlsx"):
    try:
        df = distributia_sub_categoiilor()
        print(df[2])
        header = df[0]
        workbook = xlsxwriter.Workbook(patch[0])
        worksheet = workbook.add_worksheet()
        worksheet.write_row('A1', header)
        worksheet.write_column('A2', df[1])
        worksheet.write_column('B2', df[2])
        workbook.close()
        full_path_to_file = str(patch[0])
        os.startfile(full_path_to_file)

    except BaseException as e:
        logging.exception(e)
def export_totalProfitGraph(patch="data.xlsx"):
    try:
        df = total_sales_by_subCategory()
        print(df)
        header = df[3].columns
        workbook = xlsxwriter.Workbook(patch[0])
        worksheet = workbook.add_worksheet()

        worksheet.write_row('A1', header)
        worksheet.write_column('A2', df[0])
        worksheet.write_column('B2', df[1])
        worksheet.write_column('C2', df[2])

        chart = workbook.add_chart({'type': 'column'})
        data_len = len(df[0]) + 1
        chart.add_series({
            'name': '=Sheet1!$B$1',
            'categories': f'=Sheet1!$A$2:$A${data_len}',
            'values': f'=Sheet1!$B$2:$B${data_len}',
        })
        chart.add_series({
            'name': '=Sheet1!$B$1',
            'categories': f'=Sheet1!$A$2:$A${data_len}',
            'values': f'=Sheet1!$C$2:$C${data_len}',
        })
        worksheet.insert_chart('D2', chart)
        worksheet.conditional_format(f'B2:B{data_len}', {'type': '3_color_scale'})
        worksheet.conditional_format(f'C2:C{data_len}', {'type': '3_color_scale'})

        workbook.close()
        full_path_to_file = str(patch[0])
        os.startfile(full_path_to_file)
    except BaseException as e:
        logging.exception(e)

def total_sales_by_subCategory():
    dataframe = get_data()
    df = dataframe[["Sub-Category", "Sales", "Profit"]]
    df2 = df.groupby("Sub-Category").sum()
    index = df2.index
    sales = df2["Sales"]
    profit = df2["Profit"]

    obj = [index, sales, profit, df]
    return obj

def distributia_sub_categoiilor():
    dataframe = get_data()
    # Se selecteaza coloanele Category, Sub-Category, Sales
    df = dataframe[["Category", "Sub-Category", "Sales"]]

    x = df.drop_duplicates(subset="Sub-Category")["Sub-Category"]

    # Se grupeaza datele in functie de category si sub-category
    # .size() -> count
    z = df.groupby(["Category", "Sub-Category"]).size().unstack(fill_value=0)

    y = z.index
    obj = [y, x, z]
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

    obj = [y, x, x1, x2]
    return obj
