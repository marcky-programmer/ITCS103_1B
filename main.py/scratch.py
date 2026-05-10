import openpyxl as op
workbook = op.Workbook()
sheet = workbook.active

#Headers
sheet["A1"] = "ID"
sheet["B1"] = "First Name"
sheet["C1"] = "Last Name"
sheet["D1"] = "Birth Year"
sheet["E1"] = "Age"

#Current year
current_year = 2026

#Loop for 3 favorite people
for j in range(1, 4):

    print(f"\nFavorite Person {j}")

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    birth_year = int(input("Enter Birth Year: "))

    # Calculate age
    age = current_year - birth_year

    # Save data to Excel
    sheet["A" + str(j + 1)] = j
    sheet["B" + str(j + 1)] = first_name
    sheet["C" + str(j + 1)] = last_name
    sheet["D" + str(j + 1)] = birth_year
    sheet["E" + str(j + 1)] = age

#Save workbook
workbook.save("favorite_people.xlsx")

print("\nData saved successfully!")

#Display all records
print("\nSaved Records:")

for row in sheet.iter_rows(values_only=True):
    print(row)