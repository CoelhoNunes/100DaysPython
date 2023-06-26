from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = inputs.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Buttons
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# Entry
inputs = Entry(width=10)
inputs.get()
inputs.grid(column=3, row=2)

window.mainloop()
