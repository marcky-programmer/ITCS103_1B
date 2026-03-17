import tkinter as tk

window = tk.Tk()
window.title("Profile Builder")
window.resizable(True, True)
window.geometry("1000x1000")
window.configure(bg = '#708238',cursor = 'arrow')

title = tk.Label(window,text="Profile Builder",font=("Times New Roman",20,'bold'))
title.place(x=500,y=30)

frame = tk.Frame(window)
frame.place(x=65,y=70)

def submit():
    gender = radio_val.get()
    if gender == 0:
        window.configure(bg = 'light blue')
    else:
        window.configure(bg = 'pink')
    
    year = eval(byear_ent.get())
    taon = 2026 - year
    age['text']=f"Your age is {taon}"

    


   
    full = name.get()
    name['text'] = f"{fname_ent},{mname_ent} {lname_ent} "

    

    

    
submits = tk.Button(window,text='Submit', command=submit)
submits.place(x=300,y=400)



    


fname_ent = tk.Entry(window)
fname_ent.place(x=200,y=100)

fname_label = tk.Label(window,text="First Name",font=("arial",10,"italic"))
fname_label.place(x=228,y=130)

mname_ent = tk.Entry(window)
mname_ent.place(x=350,y=100)

mname_label = tk.Label(window,text="Middle Name",font=("arial",10,"italic"))
mname_label.place(x=365,y=130)

lname_ent = tk.Entry(window)
lname_ent.place(x=500,y=100)

lname_label = tk.Label(window,text="Last Name",font=("arial",10,"italic"))
lname_label.place(x=510,y=130)

byear_ent = tk.Entry(window)
byear_ent.place(x=200,y=200)

byear_label = tk.Label(window,text='Birth Year',font=("arial",10,"italic"))
byear_label.place(x=228,y=230)

age = tk.Label(window,text="Your Age ...",font=("arial",15,"bold"))
age.place(x=400,y=225)

gender = tk.Label(window,text="Gender",font=("arial",10,"italic"))
gender.place(x=200,y=300)

radio_val = tk.IntVar()

male = tk.Radiobutton(window,text='Male', variable=radio_val, value=0)
male.place(x=300,y=300)

female = tk.Radiobutton(window,text='Female', variable=radio_val, value=1)
female.place(x=400,y=300)



toplevel = tk.Toplevel(window)

toplevel = tk.Tk()

toplevel.configure(bg = '#708238',cursor = 'arrow')

name = tk.Label(toplevel,text='')
name.place(x=5,y=7)




window.mainloop()