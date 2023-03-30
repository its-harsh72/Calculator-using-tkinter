import tkinter as tk

def add_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    label_result.config(text="Result: " + str(result))

def subtract_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 - num2
    label_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Simple Calculator")

label1 = tk.Label(root, text="Number 1:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Number 2:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button_add = tk.Button(root, text="Add", command=add_numbers)
button_add.pack()

button_subtract = tk.Button(root, text="Subtract", command=subtract_numbers)
button_subtract.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()

root.mainloop()
