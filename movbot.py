import tkinter as tk

# Window
root = tk.Tk()
root.title("Moving Robot Bot")
root.geometry("600x500")

# Canvas
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Robot parts
head = canvas.create_rectangle(270, 100, 330, 160, fill="gray")
eye1 = canvas.create_oval(285, 120, 295, 130, fill="black")
eye2 = canvas.create_oval(305, 120, 315, 130, fill="black")

body = canvas.create_rectangle(260, 160, 340, 260, fill="silver")
left_arm = canvas.create_rectangle(230, 170, 260, 240, fill="gray")
right_arm = canvas.create_rectangle(340, 170, 370, 240, fill="gray")
left_leg = canvas.create_rectangle(270, 260, 300, 330, fill="black")
right_leg = canvas.create_rectangle(300, 260, 330, 330, fill="black")

robot_parts = [
    head, eye1, eye2, body,
    left_arm, right_arm,
    left_leg, right_leg
]

# Move robot
def move(dx, dy):
    for part in robot_parts:
        canvas.move(part, dx, dy)

# Direction controls
def move_left():
    move(-10, 0)

def move_right():
    move(10, 0)

def move_up():
    move(0, -10)

def move_down():
    move(0, 10)

# Automatic movement
auto = False
def auto_walk():
    global auto
    if auto:
        move(5, 0)
        root.after(100, auto_walk)

def toggle_auto():
    global auto
    auto = not auto
    if auto:
        auto_walk()

# Buttons
controls = tk.Frame(root)
controls.pack(pady=10)
tk.Button(controls, text="⬅ Left", command=move_left, width=8).grid(row=0, column=0)
tk.Button(controls, text="➡ Right", command=move_right, width=8).grid(row=0, column=1)
tk.Button(controls, text="⬆ Up", command=move_up, width=8).grid(row=0, column=2)
tk.Button(controls, text="⬇ Down", command=move_down, width=8).grid(row=0, column=3)
tk.Button(controls, text="🤖 Auto Walk", command=toggle_auto, width=12).grid(row=0, column=4)

# Keyboard control
root.bind("<Left>", lambda e: move_left())
root.bind("<Right>", lambda e: move_right())
root.bind("<Up>", lambda e: move_up())
root.bind("<Down>", lambda e: move_down())

root.mainloop()
