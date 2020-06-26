import tkinter as tk


def uppercase():
    name = display.get()
    display.delete(0, tk.END)
    display.insert(0, name.upper())


def normalize():
    name = display.get()
    display.delete(0, tk.END)
    display.insert(0, name.title())


def lowercase():
    name = display.get()
    display.delete(0, tk.END)
    display.insert(0, name.lower())


def reverse():
    name = display.get()
    display.delete(0, tk.END)
    display.insert(0, name[::-1])


root = tk.Tk()
root.title("Name Formatter")
display = tk.Entry(root, width=55, borderwidth=5)
display.grid(row=0, column=0, columnspan=4)

button = tk.Button(root, text="Uppercase", command=uppercase)
button1 = tk.Button(root, text="Normal", command=normalize)
button2 = tk.Button(root, text="Lowercase", command=lowercase)
button3 = tk.Button(root, text="Reverse", command=reverse)
button.grid(row=1, column=0)
button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=1, column=3)

root.mainloop()