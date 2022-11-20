import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import xlsxwriter


# Construct the columns for the different powers of x


def get_r2_statsmodels(x, y, k=1):
    xpoly = np.column_stack([x ** i for i in range(k + 1)])
    return sm.OLS(y, xpoly).fit().rsquared


# Use the formula API and construct a formula describing the polynomial
def get_r2_statsmodels_formula(x, y, k=1):
    formula = 'y ~ 1 + ' + ' + '.join('I(x**{})'.format(i) for i in range(1, k + 1))
    data = {'x': x, 'y': y}
    return smf.ols(formula, data).fit().rsquared  # or rsquared_adj


def export_to_excel(obj, patch='data.xlsx'):
    try:
        date = []
        for i in obj[0]:
            date.append(i.strftime("%Y/%m/%d"))

        print(date)
        profit = obj[1].tolist()
        header = ["Order Date", "Profit"]

        workbook = xlsxwriter.Workbook('chart_line.xlsx')
        worksheet = workbook.add_worksheet()

        # Add the worksheet data to be plotted.
        worksheet.write_row('A1', header)
        worksheet.write_column('A2', date)
        worksheet.write_column('B2', profit)

        # Create a new chart object.
        chart = workbook.add_chart({'type': 'line'})

        data_len = len(profit) + 1
        # Add a series to the chart.
        chart.add_series({
            'values': f'=Sheet1!$B$2:$B${data_len}',
            'categories': f'=Sheet1!$A$2:$A${data_len}',
            'name': 'Profit/Time',
            'trendline': {
                'type': 'polynomial',
                'name': 'Profit TrendLine',
                'order': 1,
                'forward': 0.1,
                'backward': 0.2,
                'display_r_squared': True,
                'display_equation': True,
                'line': {
                    'color': 'red',
                    'width': 1,
                },
            },
        })
        # Insert the chart into the worksheet.
        worksheet.insert_chart('D2', chart)

        worksheet.conditional_format(f'B2:B{data_len}', {'type': '3_color_scale'})
        workbook.close()
    except BaseException as e:
        print(e)


def get_data():
    file_name = "Superbaza.xls"  # path to file + file name
    sheet = "superstore"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    # DataFrame (Tabel de date coloane si linii (24 coloane, 10.000 linii)
    dataframe = pd.DataFrame(df)
    return dataframe


def get_products():
    dataframe = get_data()
    all_products = dataframe["Product Name"].drop_duplicates().tolist()
    return all_products


def perioada_de_timp(product_name, date_min=None, date_max=None):
    dataframe = get_data()

    try:
        if not date_min and not date_max:
            # Se selecteaza coloana order date product name si profit din DataBase
            df = dataframe[["Order Date", "Product Name", "Profit"]]
            # Se filtreaza coloana product name in functie de product name si se ordoneaza.
            df2 = df[df["Product Name"] == product_name].sort_values(by="Order Date")

            order_date = df2["Order Date"].tolist()
            profit = df2["Profit"]
            date_min = df2["Order Date"].min()
            date_max = df2["Order Date"].max()
            print(date_min)
            print(date_max)
            obj = [order_date, profit, date_min, date_max]

            # calculate equation for trendline
            return obj
        else:
            print(date_min)
            print(date_max)

            df = dataframe[["Order Date", "Product Name", "Profit"]]
            df2 = df[df["Product Name"] == product_name].sort_values(by="Order Date")
            df_date = df2[df2["Order Date"] >= date_min]
            df_date1 = df_date[df_date["Order Date"] <= date_max]

            print(df_date1["Order Date"].min())
            order_date = df_date1["Order Date"].tolist()
            profit = df_date1["Profit"]
            obj = [order_date, profit, date_min, date_max]
            return obj

    except BaseException as e:
        print(e)


def test():
    dateframe = get_data()

    df1 = dateframe["Country"].drop_duplicates()
    df2 = dateframe["City"].drop_duplicates()
    df3 = dateframe["State"].drop_duplicates()
    df4 = dateframe["Region"].drop_duplicates()

    region = dateframe[["Region","State"]].drop_duplicates()
    region1 = region[region["Region"] == "South"]
    print(df4)
    print(region1)

    print(len(df1))
    print(len(df2))
    print(len(df3))
    print(len(df4))


def zona_de_distributie(product_name):
    dataframe = get_data()
    # Se selecteaza coloana State, Profit, Product Name
    df = dataframe[["State", "Profit", "Product Name"]]

    # Se filtreaza product name si se sorteaza datele
    df2 = df[df["Product Name"] == product_name].sort_values(by="State")
    region = df2["State"].tolist()  # Se atribui variabilei region toate statele
    profit = df2["Profit"].tolist()
    obj = [region, profit]
    return obj  # Se returneaza cele 2 liste (x, y)


def profilul_clientilor(product_name):
    dataframe = get_data()
    # Se aleg coloanele Segmentt Profit si Product Name
    df = dataframe[["Segment", "Profit", "Product Name"]]
    # Se filtreaza dupa product name
    df2 = df[df["Product Name"] == product_name]
    df3 = df[df["Product Name"] == product_name].groupby("Segment")["Profit"].apply(list)

    consumer = None
    home_office = None
    corporate = None

    for idx, item in enumerate(df3.index):
        if item == "Consumer":
            consumer = df3[idx]
        elif item == "Home Office":
            home_office = df3[idx]
        elif item == "Corporate":
            corporate = df3[idx]

    segment = df2["Segment"]
    profit = df2["Profit"]

    obj = [segment, profit]
    return obj, consumer, home_office, corporate, df3.index


if __name__ == "__main__":
    # x = profilul_clientilor("Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back")
    # export_to_excel(x)
    test()
