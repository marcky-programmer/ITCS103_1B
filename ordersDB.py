import openpyxl as op


workbook = op.Workbook()
sheet = workbook.active

sheet['a1'] = "Order Id"
sheet['b1'] = "Customer Name"
sheet['c1'] = "Product"
sheet['d1'] = "Quantity"
sheet['e1'] = "Price"
sheet['f1'] = "Total"

workbook.save("ordersDB.xlsx")