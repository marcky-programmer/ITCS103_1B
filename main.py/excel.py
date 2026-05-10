import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet['A1'] = "ID"
sheet['b1'] = "Last Name"
sheet['c1'] = "First Name"
sheet['d1'] = "Middle Name"
sheet['e1'] = "Birth Year"
sheet['f1'] = "Age"

workbook.save("excelDB.xlsx")