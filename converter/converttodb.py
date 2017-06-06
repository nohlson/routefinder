import openpyxl


wb = openpyxl.load_workbook('Markets.xlsx')

sheet = wb.get_sheet_by_name('Sheet1')

print(sheet['A1'].value)