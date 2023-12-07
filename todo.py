from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("To Do List")

# define our font 
my_font = Font(
    family= "Brush script MT", 
    size=30,
    weight="bold") 

my_frame = Frame(root)
my_frame.pack(pady=10)

# create listbox
my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg="systembuttonFace",
                  bd=0,
                  fg="#464646",
                  selectbackground="#a6a6a6",
                  highlightthickness=0,
                  activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

# create dummy list
materials = ["pray", "read", "take a nap" "buy groceries", "learn python"]
# Add 
for item in materials:
    my_list.insert(END, item)

# create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH) 

# configure the listbox to work with the scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Entry to add new Todo lists
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

# create button frame
button_frame = Button(root) 
button_frame.pack(pady=20)

# Functions
def delete_todo():
    my_list.delete(ANCHOR)

def add_todo():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_off_todo():
    pass

def uncross_todo():
    pass

# Delete To do list button
delete_button = Button(button_frame, text="Delete Todo", command=delete_todo)
add_button = Button(button_frame, text="Add Todo", command=add_todo)
cross_off_button = Button(button_frame, text="cross off Todo", command=cross_off_todo)
uncross_button = Button(button_frame, text="uncross Todo", command=uncross_todo)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)



root.mainloop()
