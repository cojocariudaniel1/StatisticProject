import os

import pandas as pd
import xlsxwriter
from matplotlib import pyplot as plt

from model.statistic_functions.form4_functions import chart_trendline


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    return dataframe

def export_to_excel(obj, patch='data.xlsx', trend_line_attrs=None):
    try:

        data = obj[0]
        profit = obj[1]

        header = ["Date", "Profit"]


        workbook = xlsxwriter.Workbook(patch[0])

        worksheet = workbook.add_worksheet()

        # Add the worksheet data to be plotted.
        worksheet.write_row('A1', header)
        worksheet.write_column('A2', data)
        worksheet.write_column('B2', profit)

        # Create a new chart object.
        chart = workbook.add_chart({'type': 'line'})

        data_len = len(profit) + 1

        if trend_line_attrs:
            chart.add_series({
                'values': f'=Sheet1!$B$2:$B${data_len}',
                'categories': f'=Sheet1!$A$2:$A${data_len}',
                'name': 'Chart',
                'trendline': chart_trendline(trend_line_attrs)
            })
        else:
            chart.add_series({
                'values': f'=Sheet1!$B$2:$B${data_len}',
                'categories': f'=Sheet1!$A$2:$A${data_len}',
                'name': 'Chart',
            })

        worksheet.insert_chart('E2', chart)
        print(trend_line_attrs)
        worksheet.conditional_format(f'B2:B{data_len}', {'type': '3_color_scale'})
        workbook.close()
        full_path_to_file = str(patch[0])
        os.startfile(full_path_to_file)
    except BaseException as e:
        print(e)

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

