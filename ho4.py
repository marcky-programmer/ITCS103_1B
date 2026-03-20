import tkinter as tk


window = tk.Tk()
window.title("Profile Builder")
window.resizable(True, True)
window.geometry("630x550")
window.configure(bg = '#d1df9d',cursor = 'arrow')

title = tk.Label(window,text="Profile Builder",font=("Times New Roman",20,'bold'),bg='#d1df9d')
title.place(x=240,y=20)

frame = tk.Frame(window,width=530,height=400,bg="#ecf2d7")
frame.place(x=50,y=70)


    
def submit():
    # gender = radio_val.get()
    # if gender == 0:
    #     window.configure(bg = 'light blue')
    #     title['bg']='light blue'
    # else:
    #     window.configure(bg = 'pink')
    #     title['bg']='pink'


    pop_up = tk.Toplevel(window)
    pop_up.title("outcome")
    pop_up.geometry("500x500")
    pop_up.configure(bg = '#d6d6d7')

    student_id = tk.Label(pop_up,text='Student ID',font=('Times New Roman', 20,'bold'),bg = '#d6d6d7')
    student_id.place(x=170,y=50)

    gender = radio_val.get()
    if gender == 0:
        pop_up.configure(bg = 'light blue')
        student_id['bg']='light blue'
    else:
        pop_up.configure(bg = 'pink')
        student_id['bg']='pink'

    p_frame = tk.Frame(pop_up,width=350,height =350,bg="#ecf2d7")
    p_frame.place(x=70,y=100)

    name = tk.Label(p_frame,text="Name:",font=("Times New Roman",20,'bold'),bg="#ecf2d7")
    name.place(x=20,y=120)

    full_name = tk.Label(p_frame,text="",font=("Times New Roman",15,'bold'),bg='#ecf2d7')
    full_name.place(x=120,y=125)

    first = fname_ent.get()
    second = mname_ent.get()
    last = lname_ent.get()
    full_name['text']= f'{first} {second} {last}'.title()

    edad = tk.Label(p_frame,text='Age:',font=("Times New Roman",20,'bold'),bg= '#ecf2d7')
    edad.place(x=20,y=180)

    label_age = tk.Label(p_frame,text="",font=("Times New Roman",15,'bold'),bg='#ecf2d7')
    label_age.place(x=120,y=185)

    year = eval(byear_ent.get())
    taon = 2026 - year
    label_age['text']=f'{taon} years old'

    gender = tk.Label(p_frame,text='Gender:',font=("Times New Roman",20,'bold'),bg="#ecf2d7")
    gender.place(x=20,y=240)

    
    gender_reveal = tk.Label(p_frame,text="",font=("Times New Roman",15,'bold'),bg='#ecf2d7')
    gender_reveal.place(x=120,y=245)

    gender = radio_val.get()
    if gender == 0:
        gender_reveal['text']='Male'
    else:
        gender_reveal['text']='Female'
     
submits = tk.Button(window,text='Submit', command=submit)
submits.place(x=300,y=400)

fname_ent = tk.Entry(window)
fname_ent.place(x=100,y=100)

fname_label = tk.Label(window,text="First Name",font=("arial",10,"italic"),bg="#ecf2d7")
fname_label.place(x=128,y=130)

mname_ent = tk.Entry(window)
mname_ent.place(x=250,y=100)

mname_label = tk.Label(window,text="Middle Name",font=("arial",10,"italic"),bg="#ecf2d7")
mname_label.place(x=270,y=130)

lname_ent = tk.Entry(window)
lname_ent.place(x=400,y=100)

lname_label = tk.Label(window,text="Last Name",font=("arial",10,"italic"),bg="#ecf2d7")
lname_label.place(x=430,y=130)

def edge(event):
    year = eval(byear_ent.get())
    taon = 2026 - year
    age['text']=f"Your age is {taon}"


byear_ent = tk.Entry(window)
byear_ent.place(x=100,y=200)

byear_ent.bind("<Return>",edge)

byear_label = tk.Label(window,text='Birth Year',font=("arial",10,"italic"),bg="#ecf2d7")
byear_label.place(x=128,y=230)

age = tk.Label(window,text="Your Age ...",font=("arial",15,"bold"),bg="#ecf2d7")
age.place(x=300,y=225)

gender = tk.Label(window,text="Gender",font=("arial",10,"italic"),bg="#ecf2d7")
gender.place(x=100,y=300)

def male_color(event):
    gender = radio_val.get()
    if gender == 0:
        window.configure(bg = 'light blue')
        title['bg']='light blue'


def female_color(event):
    gender = radio_val.get()
    if gender == 1:
        window.configure(bg='pink')
        title['bg']='pink'

window.bind("<Enter>",male_color)
window.bind("<Leave>",female_color)

#     else:
#         window.configure(bg = 'pink')
#         title['bg']='pink'

# gender.bind("<Enter>",color)


radio_val = tk.IntVar()

male = tk.Radiobutton(window,text='Male', variable=radio_val, value=0)
male.place(x=200,y=300)

female = tk.Radiobutton(window,text='Female', variable=radio_val, value=1)
female.place(x=300,y=300)






window.mainloop()