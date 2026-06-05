import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet['a1'] = "Id"
sheet['b1'] = "Name"
sheet['c1'] = "Generic Name"
sheet['d1'] = "Category"
sheet['e1'] = "Expiration Date"

workbook.save("MedicinesDb.xlsx")