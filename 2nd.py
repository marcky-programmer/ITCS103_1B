import tkinter as tk



window = tk.Tk()
window.title("GUI design")
window.resizable(True,True)
window.geometry("500x500")
window.configure(bg='#708238',cursor='arrow')

menu = tk.Menu(window)
window['menu']=menu

file_drop = tk.Menu(menu,tearoff=0)
file_drop.add_command(label="New")
file_drop.add_command(label="Open")
file_drop.add_command(label="Exit")

menu.add_cascade(label="File",menu=file_drop)

view_drop = tk.Menu(menu,tearoff=0)
view_drop.add_command(label="New")
view_drop.add_command(label="Open")
view_drop.add_command(label="Exit")

menu.add_cascade(label="View",menu=view_drop)

label = tk.Label(window,text="Hello World",bg="white",font=("Poppins",19,"bold"))
label.pack(pady=10)

frame = tk.Frame(window,bg="Grey")
frame.pack()

# scroll_1st = tk.Scrollbar(window)
# scroll_1st.pack(side = "right", fill = "y")

# scroll_2nd = tk.Scrollbar(window,orient="horizontal")
# scroll_2nd.pack(side="bottom",fill="x")

# (yscrollcommand=scroll_1st.set,xscrollcommand=scroll_2nd.set




img = tk.PhotoImage(file="mama.png")
img = img.subsample(4,4)
img_label = tk.Label(frame,image = img,text="Hirono",compound="top")
img_label.pack()

frame2 = tk.Frame(frame,bg="#708238")
frame2.pack()


label3 =tk.Label(frame,text="Username:",bg="White",font=("Poppins",19,"bold"))
label3.pack(pady=10,padx=10)

username_ent = tk.Entry(frame,show="")
username_ent.pack(padx=10)


def show():
    username = username_ent.get()
    label2=tk.Label(window,text="Button is clicked!")
    label2.pack()
    label['text'] = f"Hello, {username}"

    remember = check_val.get()
    if remember == 1:
        label4 = tk.Label(window,text="You are remembered")
        label4.pack()
    else:
        label4 = tk.Label(window,text="You are not remeberd")
        label4.pack()

    gender = radio_val.get()
    if gender == 1:
        label3 = tk.Label(window,text="You are male")
        label3.pack()
    else:
        label3 = tk.Label(window,text="You are female")
        label3.pack()

    house = listbox.curselection()
    house = listbox.get(house)
    label5=tk.Label(window,text=f"Your house is {house}")
    label5.pack()

radio_val = tk.IntVar()

female = tk.Radiobutton(frame,text="Female",variable=radio_val,value=0)
female.pack()

male = tk.Radiobutton(frame,text="Male",variable=radio_val,value=1)
male.pack()

listbox_lb1 = tk.Label(frame2,text="Choose your house:")

scroll =tk.Scrollbar(frame2)
scroll.pack(side = "right",fill = "y")
#side = "bottom",fill = "x"
scroll2 = tk.Scrollbar(frame2,orient ="horizontal")
scroll2.pack(side="bottom",fill="x")

listbox = tk.Listbox(frame2,selectmode="single",yscrollcommand=scroll.set,xscrollcommand=scroll2.set)
listbox.insert(0,"Python")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")
listbox.insert(0,"Python")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")
listbox.insert(0,"Python")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")
listbox.insert(0,"Python")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")
listbox.insert(0,"Pythonyowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")
listbox.pack()

scroll['command']=listbox.yview
scroll2['command']=listbox.xview


check_val = tk.IntVar()

check_btn = tk.Checkbutton(window,text="Remember Me", variable=check_val)
check_btn.pack()

button = tk.Button(window,text="Submit",command=show,relief="sunken",activebackground="white",activeforeground="grey")
button.pack(pady=10)

popup = tk.Toplevel(window)

popup.transient(window)
popup.grab_set()

window.title("GUI design")
window.resizable(True,True)
window.geometry("500x500")
window.configure(bg='#708238',cursor='arrow')

use_form = tk.Label(window, text="USe form")
use_form.grid()

u_name = tk.Label(window,text="Username:")
u_name.grid()

u_name = tk.Entry(window)
u_name.grid()

p_word = tk.Label(window,text="Password:")
p_word.grid()

p_word = tk.Entry(window)
p_word.grid()


log_in = tk.Button(window,text="log in",bg="red")
log_in.grid()


window.mainloop()