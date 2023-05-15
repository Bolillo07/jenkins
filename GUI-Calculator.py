from tkinter import *

def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    label_result.config(text="Result: " + str(result))

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    label_result.config(text="Result: " + str(result))

# create the GUI
root = Tk()
root.title("Calculator")

label1 = Label(root, text="Number 1")
label1.pack()

entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Number 2")
label2.pack()

entry2 = Entry(root)
entry2.pack()

button_add = Button(root, text="+", command=add)
button_add.pack()

button_subtract = Button(root, text="-", command=subtract)
button_subtract.pack()

label_result = Label(root, text="Result: ")
label_result.pack()

root.mainloop()
