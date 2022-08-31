# install openpyxl
# import os

# os.chdir("<path>")

# workbook = openpyxl.load_workbook("<filename>")
# sheet = workbook.get_sheet_by_name("Sheet 1")

# sheet_list = workbook.get_sheet_names()

# cell = sheet["A1"] => we can access the cell like we would with an array
# cell.value => returns the value in the fromatted datatype

# or we can us sheet.cell(row = 1, column = 2) => cell object

# create a spreadsheet
# wb = openpyxl.Workbook()

# wb.get_sheet_names => it shows that the file starts with 1 sheet

# sheet = wb.get_sheet_by_name("Sheet")
# sheet["A1"] = 43

# to save wb.save("./example.xls")
# to add a sheet => sheet2 = wb.create_sheet()
# to change the title of a sheet
# sheet2.title = "My new sheet name"
# or wb.create_sheet(index=[0,1,2...], title="<name>")
