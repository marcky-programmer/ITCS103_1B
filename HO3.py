import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.resizable(True, True)
window.geometry("1000x1000")
window.configure(bg = '#708238',cursor = 'arrow')

label = tk.Label(window,text="Simple Calculator",padx=250)
label.place(x=50,y=30)

no_1st = tk.Label(window,text="Enter 1st number",bg='white')
no_1st.place(x=80,y=80)

entry_1st = tk.Entry(window)
entry_1st.place(x=190,y=82)

no_2nd = tk.Label(window,text="Enter 2nd number",bg='white')
no_2nd.place(x=79,y= 110)

entry_2nd = tk.Entry(window)
entry_2nd.place(x=190,y=112)



# subtract = tk.Button(window,text="Subtract")
# subtract.place(x=200,y=150)

# multiply =tk.Button(window,text="Multiply")
# multiply.place(x=130,y=180)

# divide = tk.Button(window,text="Divide")
# divide.place(x=200,y=180)

def add():
    first = eval(entry_1st.get())
    second = eval(entry_2nd.get())
    total = first + second
    label ['text'] = f"The sum of {first} and {second} is {total}"

add = tk.Button(window,text="Add",command=add)
add.place(x=130,y=150)
    
def minus():
    first = eval(entry_1st.get())
    second = eval(entry_2nd.get())
    total = first  - second
    label ['text'] = f"The difference of {first} and {second} is {total}"

subtract = tk.Button(window,text="Subtract",command=minus)
subtract.place(x=200,y=150)

def divides():
    first = eval(entry_1st.get())
    second = eval(entry_2nd.get())
    total = first  / second
    label ['text'] = f"The quotient of {first} and {second} is {total}"

divide = tk.Button(window,text="divide",command=divides)
divide.place(x=200,y=180)

def multiplys():
    first = eval(entry_1st.get())
    second = eval(entry_2nd.get())
    total = first  * second
    label ['text'] = f"The product {first} and {second} is {total}"

multiplication = tk.Button(window,text="multiply",command=multiplys)
multiplication.place(x=130,y=180)




window.mainloop()
