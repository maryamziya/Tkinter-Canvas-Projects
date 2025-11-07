from tkinter import *

window = Tk()
window.title("** 🎨COLOR PALETTE🎨 **")
window.config(padx=10, pady=10)
canvas = Canvas(window, width=600, height=400, bg="white")
canvas.pack()

last_x = None
last_y = None
current_color = "black"

def draw_line(event):
    global last_x,last_y
    if last_x and last_y:
        canvas.create_line(last_x, last_y, event.x, event.y, fill=current_color, width=3)
        last_x = event.x
        last_y = event.y

def start_draw(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y


def stop_drawing(event):
    global last_x,last_y
    last_x = None
    last_y = None

def set_color(new_color):
    global current_color
    current_color = new_color
    color.config(text=f"Color:{current_color}")

def clear():
    canvas.delete("all")

control_frame = Frame(window, padx=10, pady=10)
control_frame.pack(side=BOTTOM, fill=X)
Button(control_frame, text="Red", command=lambda: set_color("red"),bg="red",fg="white").pack(side=LEFT, padx=5)
Button(control_frame, text="Blue", command=lambda: set_color("blue"),bg="blue",fg="white").pack(side=LEFT, padx=5)
Button(control_frame, text="Green", command=lambda: set_color("green"),bg="green",fg="white").pack(side=LEFT, padx=5)
Button(control_frame, text="Black", command=lambda: set_color("black"),bg="black",fg="white").pack(side=LEFT, padx=5)

Button(control_frame , text="Clear All",command=clear).pack(side=RIGHT, padx=15)


color = Label(text=f"Color:{current_color}",font=("Times New Roman",))
color.pack(side=LEFT, padx=5)


canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw_line)
canvas.bind("<ButtonRelease-1>", stop_drawing)

window.mainloop()