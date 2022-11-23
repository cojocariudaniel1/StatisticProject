import logging
import os

import pandas as pd
import xlsxwriter

from model.statistic_functions.form4_functions import chart_trendline


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    return dataframe

    # Evidenta celui mai prost cumparat produs dintr-o subcategorie comparativ cu categoria sa si cu totalul de categorii
    # Evidenta celui mai prost produs cumparat


def export_to_excel(obj, patch='data.xlsx', trend_line_attrs=None):
    try:
        product = obj[0]
        sales = obj[1]
        header = ["Products", "Sales"]

        workbook = xlsxwriter.Workbook(patch[0])

        worksheet = workbook.add_worksheet()
        worksheet.write_row('A1', header)
        worksheet.write_column('A2', product)
        worksheet.write_column('B2', sales)

        chart = workbook.add_chart({'type': 'line'})
        data_len = len(product) + 1

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
        worksheet.conditional_format(f'B2:B{data_len}', {'type': '3_color_scale'})
        workbook.close()
        full_path_to_file = str(patch[0])
        os.startfile(full_path_to_file)
    except BaseException as e:
        logging.exception(e)


def get_subcategory():
    df = get_data()
    return df["Sub-Category"].drop_duplicates().tolist()


# Evidenta celui mai prost produs cumparat
def evcmppc(subcategory, nr_product):
    df = get_data()
    dataframe = df[["Product ID", "Sales", "Category", "Sub-Category"]]
    sub_category = dataframe[dataframe["Sub-Category"] == subcategory]
    if nr_product == 0:
        return [[], []]
    result = sub_category.groupby("Product ID").mean(numeric_only=True). \
        sort_values(by="Sales", ascending=True).head(nr_product)

    values = []

    for k in result.values:
        values.append(k[0])

    index = result.index
    obj = [index, values]
    return obj
