import tkinter as tk

window = tk.Tk()

window.title("GUI design")
window.resizable(True,True)
window.geometry("500x500")
window.configure(bg='#708238',cursor='arrow')

use_form = tk.Label(window, text="Use form",bg="#708238",font=("Poppins",19,"bold"))
use_form.place(x=200,y=5)

u_name = tk.Label(window,text="Username:",bg="#708238")
u_name.place(x=150,y=50)

u_names = tk.Entry(window)
u_names.place(x=250,y=50)

p_word = tk.Label(window,text="Password:",bg="#708238")
p_word.place(x=150,y=70)

p_words = tk.Entry(window)
p_words.place(x=250,y=70)


log_in = tk.Button(window,text="log in")
log_in.place(x=300,y=110)

def enter(event):
    log_in['bg'] = "blue"


def enter(event):
    log_in['bg'] = "blue"

def entry(event):
    user = u_names.get()
    print(user)


log_in.bind("<Button-1>",enter)
log_in.bind("<Enter>",enter)
u_names.bind("<Key>",entry)

window.mainloop()