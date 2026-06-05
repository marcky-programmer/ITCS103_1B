import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet["a1"] = "ID"
sheet["b1"] = "Company"
sheet["c1"] = "Supplier Name"
sheet["d1"] = "Contact No"
sheet["e1"] = "Email"
sheet["f1"] = "Address"

workbook.save("SupplierDB.xlsx")
