import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Global expression string to keep track of inputs
expression = ""

# Function to update the expression
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

# Function to evaluate the expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        input_text.set(total)
        expression = total  # So next press continues from result
    except Exception as e:
        input_text.set("Error")
        expression = ""

# Function to clear the expression
def clear():
    global expression
    expression = ""
    input_text.set("")

# StringVar to update the input field
input_text = tk.StringVar()

# Input field
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 20), bd=10, relief='sunken', width=20, justify='right')
input_field.grid(row=0, column=0)

# Button frame
btn_frame = tk.Frame(root)
btn_frame.pack()

# List of button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Dynamically create buttons
row = 0
col = 0
for btn in buttons:
    action = lambda x=btn: press(x) if x not in ['='] else equalpress()
    tk.Button(btn_frame, text=btn, width=6, height=2, font=('arial', 18), command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text='Clear', width=20, height=2, font=('arial', 14), command=clear, bg='red', fg='white').pack(pady=10)

# Run the GUI loop
root.mainloop()
