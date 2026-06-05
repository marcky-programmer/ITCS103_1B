import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet["a1"]="ID"
sheet["b1"]="Medicines"
sheet["c1"]="Quantity"
sheet["d1"]="Status"
sheet["e1"]="Date"

workbook.save("InventoryDB.xlsx")