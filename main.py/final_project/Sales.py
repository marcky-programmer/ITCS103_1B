import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet["a1"]="Id"
sheet["b1"]="Medicine"
sheet["c1"]="Quantity"
sheet["d1"]="Price"
sheet["d1"]="Total"

workbook.save("SalesDB.xlsx")
