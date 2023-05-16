import tkinter as tk
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
    root = tk.Tk()
    root.title("Calculator")

    # create the frames
    top_frame = tk.Frame(root)
    top_frame.pack(side=tk.TOP)

    middle_frame = tk.Frame(root)
    middle_frame.pack(side=tk.TOP)

    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side=tk.TOP)

    # create the input fields
    label1 = tk.Label(top_frame, text="Number 1:", font=("Arial", 12))
    label1.pack(side=tk.LEFT, padx=10, pady=10)

    entry1 = tk.Entry(top_frame, width=10, font=("Arial", 12))
    entry1.pack(side=tk.LEFT, padx=10, pady=10)

    label2 = tk.Label(top_frame, text="Number 2:", font=("Arial", 12))
    label2.pack(side=tk.LEFT, padx=10, pady=10)

    entry2 = tk.Entry(top_frame, width=10, font=("Arial", 12))
    entry2.pack(side=tk.LEFT, padx=10, pady=10)

    # create the buttons
    button_add = tk.Button(middle_frame, text="+", font=("Arial", 16), width=5, height=2, command=lambda: label_result.config(text="Result: " + str(add(float(entry1.get()), float(entry2.get())))))
    button_add.pack(side=tk.LEFT, padx=10, pady=10)

    button_subtract = tk.Button(middle_frame, text="-", font=("Arial", 16), width=5, height=2, command=lambda: label_result.config(text="Result: " + str(subtract(float(entry1.get()), float(entry2.get())))))
    button_subtract.pack(side=tk.LEFT, padx=10, pady=10)

    button_multiply = tk.Button(middle_frame, text="*", font=("Arial", 16), width=5, height=2, command=lambda: label_result.config(text="Result: " + str(multiply(float(entry1.get()), float(entry2.get())))))
    button_multiply.pack(side=tk.LEFT, padx=10, pady=10)

    button_divide = tk.Button(middle_frame, text="/", font=("Arial", 16), width=5, height=2, command=lambda: label_result.config(text="Result: " + str(divide(float(entry1.get()), float(entry2.get())))))
    button_divide.pack(side=tk.LEFT, padx=10, pady=10)

    # create the result label
    label_result = tk.Label(bottom_frame, text="Result: ", font=("Arial", 12))
    label_result.pack(side=tk.LEFT, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
