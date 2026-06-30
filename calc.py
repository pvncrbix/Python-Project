import tkinter as tk

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""

# Function to update text
def press(num):
    global expression
    expression += str(num)
    equation_label.set(expression)

# Function to calculate result
def equal_press():
    global expression
    try:
        result = str(eval(expression))
        equation_label.set(result)
        expression = result
    except:
        equation_label.set("Error")
        expression = ""

# Clear function
def clear():
    global expression
    expression = ""
    equation_label.set("")

# String variable for display
equation_label = tk.StringVar()

# Display Entry
display = tk.Entry(root, textvariable=equation_label, font=("Arial", 20), justify="right")
display.pack(fill="both", ipadx=8, ipady=20)

# Button frame
btn_frame = tk.Frame(root)
btn_frame.pack()

# Button layout
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        action = equal_press
    else:
        action = lambda x=text: press(x)

    tk.Button(btn_frame, text=text, width=5, height=2,
              font=("Arial", 16), command=action).grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 16), command=clear)
clear_btn.pack(fill="both", padx=10, pady=10)

# Run the GUI
root.mainloop()