import os

import pandas as pd
import xlsxwriter


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    return dataframe


def export_to_excel(obj, patch='data.xlsx', trend_line_attrs=None):
    try:

        # obj = [discount, sales, profit]
        discount = obj[0]
        sales = obj[1]
        profit = obj[2]

        header = ["discount", "sales", "profit"]
        workbook = xlsxwriter.Workbook(patch[0])

        worksheet = workbook.add_worksheet()

        # Add the worksheet data to be plotted.
        worksheet.write_row('A1', header)
        worksheet.write_column('A2', discount)
        worksheet.write_column('B2', sales)
        worksheet.write_column('C2', profit)

        # Create a new chart object.
        chart = workbook.add_chart({'type': 'line'})

        data_len = len(profit) + 1
        # Add a series to the chart.

        chart.add_series({'values': f'=Sheet1!$C$2:$C${data_len}', 'categories': f'=Sheet1!$A$2:$A${data_len}'})
        chart.add_series({'values': f'=Sheet1!$A$2:$A${data_len}', 'categories': f'=Sheet1!$A$2:$A${data_len}'})

        if trend_line_attrs:
            chart.add_series({
                'values': f'=Sheet1!$B$2:$B${data_len}',
                'categories': f'=Sheet1!$A$2:$A${data_len}',
                'name': 'Profit/Time',
                'trendline': chart_trendline(trend_line_attrs)
            })
        # Insert the chart into the worksheet.
        worksheet.insert_chart('E2', chart)
        print(trend_line_attrs)
        worksheet.conditional_format(f'B2:B{data_len}', {'type': '3_color_scale'})
        worksheet.conditional_format(f'C2:C{data_len}', {'type': '3_color_scale'})
        workbook.close()
        full_path_to_file = str(patch[0])
        os.startfile(full_path_to_file)
    except BaseException as e:
        print(e)


def chart_trendline(trend_line_attrs):
    if trend_line_attrs["type"] == "polynomial":
        return {

            'type': trend_line_attrs['type'],
            'name': trend_line_attrs['name'],
            'order': trend_line_attrs['order'],
            'forward': trend_line_attrs['forward'],
            'backward': trend_line_attrs['backward'],
            'display_r_squared': trend_line_attrs['r_square'],
            'display_equation': trend_line_attrs['equation'],
            'line': {
                'color': trend_line_attrs['line_color'],
                'width': trend_line_attrs['line_width'],
            },
        }
    elif trend_line_attrs["type"] == "moving_average":
        return {
            'type': trend_line_attrs["type"],
            'name': trend_line_attrs['name'],
            'period': trend_line_attrs["period"],
            'line': {
                'color': trend_line_attrs['line_color'],
                'width': trend_line_attrs['line_width'],
            },
        }
    elif trend_line_attrs["type"] == "linear" or trend_line_attrs["type"] == "exponential":
        return {
            'type': trend_line_attrs["type"],
            'name': trend_line_attrs['name'],
            'intercept': trend_line_attrs["intercept"],
            'display_r_squared': trend_line_attrs['r_square'],
            'display_equation': trend_line_attrs['equation'],
            'forward': trend_line_attrs['forward'],
            'backward': trend_line_attrs['backward'],
            'line': {
                'color': trend_line_attrs['line_color'],
                'width': trend_line_attrs['line_width'],

            },
        }
    elif trend_line_attrs["type"] == "power":
        return {
            "type": trend_line_attrs["type"],
            "name": trend_line_attrs["name"],
            'line': {
                'color': trend_line_attrs['line_color'],
                'width': trend_line_attrs['line_width'],

            },
        }
    elif trend_line_attrs["type"] == "log":
        return {
            "type": trend_line_attrs["type"],
            "name": trend_line_attrs["name"],
            'line': {
                'color': trend_line_attrs['line_color'],
                'width': trend_line_attrs['line_width'],

            },
        }

def get_products():
    dataframe = get_data()
    all_products = dataframe["Product Name"].drop_duplicates()
    return all_products


def evolutia_dis_vanz(product_name):
    df = get_data()
    product = df[["Product Name", "Discount", "Sales", "Profit"]].sort_values(ascending=False, by="Discount")
    uq_product = product[product["Product Name"] == str(product_name)]

    # Se selecteaza cele 3 liste dupa ce au fost filtrate in baza de date in functie de numele la produs
    discount = uq_product["Discount"].tolist()
    sales = uq_product["Sales"].tolist()
    profit = uq_product["Profit"].tolist()

    obj = [discount, sales, profit]
    return obj
