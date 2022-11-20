Westinghouse Mesh Shade Clip-On Gooseneck Lamp, Black

        print('in export function')

        print(obj)
        index, x, y, z = obj[4], obj[1], obj[2], [3]

        x_len = len(x) + 1
        y_len = len(y) + 1
        z_len = len(z) + 1

        max_len = max([x_len, y_len, z_len]) + 2
        print(patch)
        if patch == 'data.xlsx':
            patch = ['data.xlsx']
        workbook = xlsxwriter.Workbook(str(f"{patch[0]}"))
        worksheet = workbook.add_worksheet()
        chart1 = workbook.add_chart({'type': 'line'})
        print(x, y, z)
        worksheet.write_row('A1', index)

        if x:
            worksheet.write_column('A2', x)
            worksheet.write_column(f"A{max_len + 1}", [sum(x)])
            worksheet.write_column(f"A{max_len}", ["TOTAL"])

        if y:
            worksheet.write_column('B2', y)
            worksheet.write_column(f"B{max_len + 1}", [sum(y)])
            worksheet.write_column(f"B{max_len}", ["TOTAL"])

        if z:
            worksheet.write_column('C2', z)
            worksheet.write_column(f"C{max_len + 1}", [sum(z)])
            worksheet.write_column(f"C{max_len}", ["TOTAL"])

        # Configure a second series. Note use of alternative syntax to define ranges.
        chart1.add_series({
            'name': '=Sheet1!$A$1',
            'values': f'=Sheet1!$A{max_len + 1}',
            'categories': '=Sheet1!$A$1',
        })
        chart1.add_series({
            'name': '=Sheet1!$B$1',
            'values': f'=Sheet1!$B{max_len + 1}',
            'categories': '=Sheet1!$B$1',
        })
        chart1.add_series({
            'name': '=Sheet1!$C$1',
            'values': f'=Sheet1!$C{z_len + 1}',
            'categories': '=Sheet1!$C$1',
        })
        # Add a chart title and some axis labels.
        # Set an Excel chart style.
        chart1.set_y_axis({'name': 'Profil'})
        # Insert the chart into the worksheet (with an offset).
        worksheet.insert_chart('E2', chart1, {'x_offset': 25, 'y_offset': 10})
        workbook.close()