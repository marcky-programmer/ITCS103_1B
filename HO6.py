import openpyxl as op
workbook = op.Workbook()
sheet = workbook.active

sheet["a1"] = "Id"
sheet["b1"] = "First Name"
sheet["c1"] = "Last Name"
sheet["d1"] = "Birth Year"
sheet["e1"] = "Age"

for id in range(1,4):
    print(f"Person {id}")
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    byear = int(input("Enter your birth year: "))
    age = 2026 - byear

    sheet["a"+str(1+id)] = id
    sheet["b"+str(1+id)] = fname
    sheet["c"+str(1+id)] = lname
    sheet["d"+str(1+id)] = byear
    sheet["e"+str(1+id)] = age
workbook.save("fave_peep.xlsx")

for row in sheet.iter_rows(values_only=True):
    print(row)