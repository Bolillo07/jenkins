from tkinter import *

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: division by zero"
    else:
        return num1 / num2

def main():
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

    button_add = Button(root, text="+", command=lambda: label_result.config(text="Result: " + str(add(float(entry1.get()), float(entry2.get())))))
    button_add.pack()

    button_subtract = Button(root, text="-", command=lambda: label_result.config(text="Result: " + str(subtract(float(entry1.get()), float(entry2.get())))))
    button_subtract.pack()

    button_multiply = Button(root, text="*", command=lambda: label_result.config(text="Result: " + str(multiply(float(entry1.get()), float(entry2.get())))))
    button_multiply.pack()

    button_divide = Button(root, text="/", command=lambda: label_result.config(text="Result: " + str(divide(float(entry1.get()), float(entry2.get())))))
    button_divide.pack()

    label_result = Label(root, text="Result: ")
    label_result.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
