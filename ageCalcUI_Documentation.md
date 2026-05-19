# Age Calculator UI - Code Documentation

## Overview
This is a **GUI application** using tkinter that manages a database of person records (name, birth year, age) stored in an Excel file. It allows users to create, read, update, and delete person records through an interactive interface.

---

## Table of Contents
1. [Imports](#imports)
2. [Functions](#functions)
3. [GUI Setup](#gui-setup)
4. [Widget Details](#widget-details)
5. [Application Flow](#application-flow)

---

## Imports

```python
import tkinter as tk
import openpyxl as op
from tkinter import ttk, messagebox
```

### Explanation:

| Import | Purpose |
|--------|---------|
| `tkinter as tk` | Library for creating GUI windows and interactive widgets |
| `openpyxl as op` | Library for reading, writing, and manipulating Excel files |
| `ttk` | Themed tkinter widgets that provide a modern, polished look |
| `messagebox` | Module for displaying popup windows (errors, success messages, confirmations) |

---

## Functions

### 1. `display()` - Load and Display All Records

**Purpose**: Refreshes the table with all current records from the Excel database.

```python
def display():
    workbook = op.load_workbook("excelDB.xlsx")  # Opens the Excel file
    sheet = workbook.active                       # Gets the currently active sheet
    
    # Clear all existing rows from the table
    for content in tree.get_children():
        tree.delete(content)
    
    # Read rows from Excel starting at row 2 (skip header)
    for rows in sheet.iter_rows(min_row=2, values_only=True):
        tree.insert("", tk.END, values=rows)  # Insert each row into the table
```

**Syntax Breakdown**:
- `op.load_workbook(filename)`: Opens Excel file and returns workbook object
- `workbook.active`: Returns the active sheet in the workbook
- `tree.get_children()`: Returns all rows in the Treeview table
- `sheet.iter_rows(min_row=2, values_only=True)`: Iterates through Excel rows starting at row 2, returning only values
- `tree.insert(parent, index, values)`: Inserts a new row in the table

---

### 2. `validation()` - Validate Form Input

**Purpose**: Ensures all required form fields are filled and birth year is a valid number.

```python
def validation():
    first = fname_entry.get()      # Retrieve first name from entry field
    middle = mname_entry.get()     # Retrieve middle name from entry field
    last = lname_entry.get()       # Retrieve last name from entry field
    birth = birth_entry.get()      # Retrieve birth year from entry field
    
    # Check if any field is empty
    if not first or not middle or not last or not birth:
        messagebox.showerror("Error", "All fields are required")
        return False
    
    # Check if birth year contains only digits
    if not birth.isdigit():
        messagebox.showerror("Error", "Birth year should be a number")
        return False
    
    return True  # All validations passed
```

**Syntax Breakdown**:
- `.get()`: Gets the text value from an Entry widget
- `not string`: Returns True if string is empty
- `.isdigit()`: Returns True if string contains only digits
- `messagebox.showerror(title, message)`: Displays error popup

**Return Value**:
- `True` if all validations pass
- `False` if validation fails

---

### 3. `create()` - Add a New Record

**Purpose**: Creates a new person record in the Excel database and refreshes the table.

```python
def create():
    if not validation():  # Validate form before proceeding
        return
    
    # Retrieve and store form values
    first = fname_entry.get()
    middle = mname_entry.get()
    last = lname_entry.get()
    birth = int(birth_entry.get())  # Convert birth year to integer
    
    age = 2026 - birth  # Calculate age (current year - birth year)
    
    # Open Excel file and get active sheet
    workbook = op.load_workbook('excelDB.xlsx')
    sheet = workbook.active
    
    new_id = sheet.max_row  # Use max row number as the new ID
    
    # Add new row to Excel: [ID, Last Name, First Name, Middle Name, Birth Year, Age]
    sheet.append([new_id, last, first, middle, birth, age])
    workbook.save("excelDB.xlsx")  # Save changes to Excel file
    
    # Show success message
    messagebox.showinfo("Success", "Record added successfully")
    
    display()  # Refresh table to show new record
```

**Syntax Breakdown**:
- `int(string)`: Converts string to integer
- `sheet.max_row`: Property that returns the highest row number in use
- `sheet.append(list)`: Adds a new row with the list values to the sheet
- `workbook.save(filename)`: Saves changes to Excel file
- `messagebox.showinfo(title, message)`: Displays success popup

**Data Structure**:
- ID, Last Name, First Name, Middle Name, Birth Year, Age

---

### 4. `auto_populate(event)` - Fill Form When Row Selected

**Purpose**: Automatically fills the form fields with data from a clicked table row.

```python
def auto_populate(event):
    selected = tree.focus()           # Get the focused (selected) row
    values = tree.item(selected, "values")  # Extract data from selected row
    
    if values:  # Only proceed if a row is selected
        # Clear all entry fields
        lname_entry.delete(0, tk.END)
        fname_entry.delete(0, tk.END)
        mname_entry.delete(0, tk.END)
        birth_entry.delete(0, tk.END)
        
        # Fill entry fields with selected row data
        lname_entry.insert(0, values[1])   # values[1] = Last name
        fname_entry.insert(0, values[2])   # values[2] = First name
        mname_entry.insert(0, values[3])   # values[3] = Middle name
        birth_entry.insert(0, values[4])   # values[4] = Birth year
```

**Syntax Breakdown**:
- `tree.focus()`: Returns the ID of the focused (selected) item in the table
- `tree.item(item_id, key)`: Returns information about an item (key can be "values", "text", etc.)
- `.delete(start, end)`: Deletes text from position start to end
  - `0` = beginning
  - `tk.END` = end
- `.insert(position, text)`: Inserts text at the specified position
- `values[index]`: Accesses element in tuple (0=ID, 1=Last, 2=First, 3=Middle, 4=BirthYear, 5=Age)

**Event Binding**:
This function is called whenever a user clicks on a row in the table (bound to `<<TreeviewSelect>>` event).

---

### 5. `update()` - Modify an Existing Record

**Purpose**: Updates an existing record in the Excel database with new values from the form.

```python
def update():
    selected = tree.focus()  # Get the selected row
    
    # Check if a record is selected
    if not selected():
        messagebox.showinfo("Error", "Select a record first")
    
    # Validate form input
    if not validation():
        return
    
    # Get updated values from form
    first = fname_entry.get()
    middle = mname_entry.get()
    last = lname_entry.get()
    birth = birth_entry.get()
    
    age = 2026 - birth  # Recalculate age
    
    # Get the ID of the selected record
    values = tree.item(selected, "values")
    record_id = values[0]
    
    # Open Excel file
    workbook = op.load_workbook("excelDB.xlsx")
    sheet = workbook.active
    
    # Find and update matching record
    for rows in sheet.iter_rows(main_row=2):
        if str(record_id) == str(rows[0].value):  # If record ID matches
            rows[1].value = last        # Update last name
            rows[2].value = first       # Update first name
            rows[3].value = middle      # Update middle name
            rows[4].value = birth       # Update birth year
            rows[5].value = age         # Update age
        
        workbook.save("excelDB.xlsx")  # Save changes
        messagebox.showinfo("Success", "Record updated successfully")
        display()  # Refresh table
```

**Syntax Breakdown**:
- `sheet.iter_rows(main_row=2)`: Iterates through Excel rows starting at row 2
- `rows[index].value`: Accesses and modifies the value of a cell in the row
- String comparison ensures both values are compared as strings

**Process Flow**:
1. Get selected row from table
2. Get form values and validate
3. Find matching record in Excel by ID
4. Update all fields for that record
5. Save file and refresh display

---

### 6. `delete()` - Remove a Record

**Purpose**: Deletes a selected record from the Excel database after user confirmation.

```python
def delete():
    selected = tree.focus()  # Get the selected row
    
    # Check if a record is selected
    if not selected:
        messagebox.showerror("Error", "Select a record first")
    
    # Ask user to confirm deletion
    confirm = messagebox.askyesnocancel("Confirm", "Are you sure you want to delete this?")
    
    if not confirm:  # If user clicks "No" or "Cancel"
        return  # Exit function without deleting
    
    # Get the ID of the record to delete
    values = tree.item(selected, "values")
    record_id = values[0]
    
    # Open Excel file
    workbook = op.load_workbook("excelDB.xlsx")
    sheet = workbook.active
    
    # Find and delete matching row
    for i, row in enumerate(sheet.iter_rows(min_row=2), start=2):
        if str(record_id) == str(row[0].value):  # If record ID matches
            sheet.delete_rows(i)  # Delete the row
            break  # Exit loop after deleting
    
    # Save changes and refresh
    workbook.save("excelDB.xlsx")
    messagebox.showinfo("Success", "Record deleted")
    display()  # Refresh table
```

**Syntax Breakdown**:
- `messagebox.askyesnocancel(title, message)`: Shows confirmation dialog
  - Returns True if "Yes", False if "No", None if "Cancel"
- `enumerate(iterable, start)`: Returns index and value pairs
  - `start=2` means indexing starts at 2 (matches Excel row numbers)
- `sheet.delete_rows(row_num)`: Deletes a specific row from the sheet
- `break`: Exits the loop immediately after finding and deleting the record

**Safety Features**:
- Checks if a record is selected
- Asks for user confirmation before deleting
- Only deletes the matching record by ID

---

## GUI Setup

### Window Configuration

```python
window = tk.Tk()
window.title("Age Calculator")
window.configure(bg="lightgreen")
```

**Syntax Breakdown**:
- `tk.Tk()`: Creates the main window
- `.title(text)`: Sets the window title in the title bar
- `.configure(option=value)`: Sets window properties
  - `bg`: Background color

---

## Widget Details

### Title Label

```python
title = tk.Label(window, text="Profile Builder", 
                 font=("Times New Roman", 14, "bold"),
                 bg="lightgreen")
title.grid(row=0, column=0, columnspan=6)
```

**Widget Class**: `tk.Label`
- Creates static text display
- `text`: The text to display
- `font`: Tuple of (font_name, size, style) where style is "bold", "italic", or "bold italic"
- `bg`: Background color

**Layout**: `.grid(row, column, columnspan)`
- `row`: Grid row position (0-based)
- `column`: Grid column position (0-based)
- `columnspan`: Number of columns to span

---

### Frame (Container)

```python
genframe = tk.Frame(window, bg="lightgreen", bd=2, relief="groove")
genframe.grid(row=1, column=0, columnspan=6, padx=10, pady=10)
```

**Widget Class**: `tk.Frame`
- Creates a container to group other widgets
- `bg`: Background color
- `bd`: Border width in pixels
- `relief`: Border style ("flat", "groove", "ridge", "raised", "sunken")

**Padding**:
- `padx`: Horizontal padding (left, right)
- `pady`: Vertical padding (top, bottom)

---

### Entry Fields (Input Boxes)

```python
fname_entry = tk.Entry(genframe, font=("Poppins", 12))
fname_entry.grid(row=2, column=1, columnspan=2, padx=(10,0), pady=(10,0))
```

**Widget Class**: `tk.Entry`
- Creates a single-line text input field
- `font`: Font specification (name, size)
- `.get()`: Retrieves the text entered
- `.delete(start, end)`: Removes text
- `.insert(position, text)`: Adds text at position

**Padding Syntax**:
- `padx=(10, 0)`: 10 pixels left, 0 pixels right
- `pady=(10, 0)`: 10 pixels top, 0 pixels bottom

---

### Labels

```python
fname_label = tk.Label(genframe, text="First Name",
                       font=("Poppins", 10, "italic"),
                       bg="lightgreen")
fname_label.grid(row=3, column=1, columnspan=2)
```

**Widget Class**: `tk.Label`
- Displays descriptive text for input fields
- `text`: Label text
- `font`: Font specification (name, size, style)

---

### Buttons

```python
submit_btn = tk.Button(window, text="Submit",
                       font=("Poppins", 12, "bold"),
                       bg="lightpink", fg="black",
                       command=create)
submit_btn.grid(row=6, column=0, columnspan=6, pady=(10, 20))
```

**Widget Class**: `tk.Button`
- Creates clickable button
- `text`: Button label text
- `font`: Font specification
- `bg`: Background color
- `fg`: Foreground (text) color
- `command`: Function to call when clicked (do NOT include parentheses: `command=function_name`)

**Common Properties**:
- `.grid()`: Place button in grid layout
- Multiple buttons can share same function or have different functions

---

### Table (Treeview)

```python
tree = ttk.Treeview(window, columns=("ID","Last","First","Middle","BirthYear","Age"),
                    show="headings")

for col in ("ID","Last","First","Middle","BirthYear","Age"):
    tree.heading(col, text=col)

tree.grid(row=7, column=0, columnspan=4)
tree.bind("<<TreeviewSelect>>", auto_populate)
```

**Widget Class**: `ttk.Treeview`
- Creates a table/tree widget for displaying tabular data
- `columns`: Tuple of column names
- `show`: What to display ("headings" hides the first column, "tree headings" shows both)

**Methods**:
- `.heading(col_name, text)`: Sets the header text for a column
- `.insert(parent, index, values)`: Adds a row to the table
  - `parent`: "" means root level (for simple tables)
  - `index`: tk.END adds to the end
  - `values`: Tuple of values for each column
- `.get_children()`: Returns all rows
- `.delete(item_id)`: Removes a row
- `.focus()`: Returns the selected row
- `.item(item_id, key)`: Gets information about an item

**Event Binding**:
- `.bind(event, callback)`: Connects events to functions
- `"<<TreeviewSelect>>"`: Event fired when user selects a row
- Callback function receives an event object as parameter

---

## Application Flow

### Startup Sequence

```python
display()           # Load all records from Excel
window.mainloop()   # Start the GUI event loop
```

**Process**:
1. Application starts
2. `display()` loads all records from `excelDB.xlsx` into the table
3. `window.mainloop()` keeps the window open and responsive
4. Event loop processes:
   - Button clicks (Submit, Update, Delete)
   - Table row selections (auto-populate form)
   - User input in entry fields

### User Interaction Flow

#### Creating a Record:
1. User fills in First Name, Middle Name, Last Name, Birth Year
2. User clicks "Submit" button
3. `create()` function:
   - Validates all fields are filled and birth year is numeric
   - Calculates age
   - Adds row to Excel
   - Shows success message
   - Calls `display()` to refresh table

#### Selecting and Updating:
1. User clicks on a row in the table
2. `auto_populate()` automatically fills form with that record's data
3. User modifies any fields
4. User clicks "Update" button
5. `update()` function:
   - Validates form
   - Finds record by ID
   - Updates all fields in Excel
   - Refreshes table

#### Deleting:
1. User clicks on a row in the table
2. User clicks "Delete" button
3. `delete()` function:
   - Asks for confirmation
   - Removes row from Excel if confirmed
   - Refreshes table

---

## Data Structure

### Excel File Format (`excelDB.xlsx`)

| Column | Data Type | Example |
|--------|-----------|---------|
| ID | Integer | 2 |
| Last Name | String | "Smith" |
| First Name | String | "John" |
| Middle Name | String | "Michael" |
| Birth Year | Integer | 2000 |
| Age | Integer | 26 |

**Row Structure**:
- Row 1: Headers (ID, Last, First, Middle, BirthYear, Age)
- Row 2+: Actual data records

---

## Summary

This application demonstrates:
- **GUI Development**: tkinter widgets and layout management
- **File I/O**: Reading and writing Excel files with openpyxl
- **CRUD Operations**: Create, Read, Update, Delete functionality
- **Data Validation**: Input checking before database operations
- **Event Handling**: Button clicks and table selections
- **User Feedback**: Success/error messages and auto-population

The application is fully functional for managing a simple person database with automatic age calculation based on birth year.
