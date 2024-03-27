# import tkinter
from tkinter import *
from tkinter.ttk import *  # we override the original widgets with the new theme of ttk which look better

# Initialize a tkinter window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)  # we can add padding inside the main window

# Label
my_label = Label(text="I Am a Label", font=("Arial", 20, "normal"))
my_label["text"] = "Other Text"  # we can pass parameter values by calling the attribute name like in a dictionary
my_label.config(text="New Text")  # or we can use the .config() function
# my_label.pack()  # we must first create a component and then specify a layout on the screen. For that we use pack()
# my_label.place(x=100, y=200)  # we can use place() too which is more precise
my_label.grid(column=0, row=0)  # or we can use grid() which is easier to use. It positions elements relative to others
# my_label.config(padx=50, pady=50)  # we can also add padding around objects but this syntax doesn't work for ttk
my_label.config(padding=[50, 50])  # we must use this syntax where padding= expects a list of up to 4 values [l,t,r,b]

# Button
button.config(padding=[50, 50])

def button_clicked():
    print("I got clicked")
    new_text = my_input.get()  # .get() returns whatever is on the text field currently
    my_label.config(text=new_text)


my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

my_button2 = Button(text="New Button", command=button_clicked)
my_button2.grid(column=2, row=0)

# Entry
my_input = Entry(width=10)
my_input.grid(column=3, row=2)


window.mainloop()  # loop that keeps the screen running. Must be at the end of program
