# PROGRAM TO MAKE A CALCULATOR IN GUI

import tkinter as tk


def on_button_click(button_value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + button_value)


def clear_entry():
    entry.delete(0, tk.END)


def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the input and result
entry = tk.Entry(root, width=20, font=('Arial', 20), bd=10, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Creating and placing the buttons in the grid
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2,
              command=lambda b=button: on_button_click(b) if b != '=' else calculate_result()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text='C', width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)

# Run the Tkinter event loop
root.mainloop()
