from tkinter import *
from tkinter.ttk import *  # overwrite with ttk widgets for a better look

LABELS_PADDING = [5]
FONT = ("Ink Free", 18, "bold")


# Convert function
def miles_to_kilometers():
    miles = float(miles_entry.get())
    km = round(miles * 1.609344, 6)
    kilometer_result_label.config(text=f"{km}")


# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=150, height=150)
window.config(padx=20, pady=20)  # padding inside main window

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padding=LABELS_PADDING, font=FONT)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padding=LABELS_PADDING, font=FONT)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)
kilometer_result_label.config(padding=LABELS_PADDING, font=FONT)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)
kilometer_label.config(padding=LABELS_PADDING, font=FONT)


# Button
button1 = Button(text="Calculate", command=miles_to_kilometers)
button1.grid(column=1, row=2)

# Entry
miles_entry = Entry(width=7, font=FONT)
miles_entry.focus()
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)


window.mainloop()
