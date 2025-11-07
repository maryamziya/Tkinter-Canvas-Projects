# Dynamic Score Tracker with Bars
# This problem moves away from text/images and focuses on using canvas.create_rectangle() to dynamically draw and resize shapes, simulating a graphical score or health bar.
#
# Instructions 📊
# Setup & Variables:
#
# Create the main window and a Canvas widget.
from tkinter import *

window = Tk()
canvas = Canvas()
canvas.pack()
#
# Define two simple Python variables, e.g., SCORE_A = 80 and SCORE_B = 40, representing the current scores out of 100.
score_a = 0
score_b = 0
# Create two Button widgets labeled "Add Point to A" and "Add Point to B" (or "Increase A" and "Increase B").
increase_a = Button(text="Increase A by one point")
increase_b = Button(text="Increase B by one point")
increase_a.pack()
increase_b.pack()
# Draw the Initial Bars:
#
# Use canvas.create_rectangle() twice to draw the initial bars for Score A and Score B.
# Hint: The coordinates for a rectangle are (x1, y1, x2, y2). The starting X-coordinate (x1) should be constant (e.g., 50). The ending X-coordinate (x2) should be calculated based on the score (e.g., 50 + SCORE_A * multiplier). Store the IDs of these two rectangles (bar_a_id, bar_b_id).

r_1 = canvas.create_rectangle(50,10,50 + score_a * 2,20,fill = "#e2979c",outline="#FFC0CB")
r_2 = canvas.create_rectangle(50,40,50 + score_b * 2,50,fill = "#FFB6C1",outline="#FFE4E1")
# canvas.create_rectangle()

# Add labels using canvas.create_text() next to the bars (e.g., "Score A").
a = canvas.create_text(27,15,text="Score A",font=("Times New Roman",7,"bold"))
b = canvas.create_text(27,45,text="Score B",font=("Times New Roman",7,"bold"))
# Define the update_bars Function:
# Create a function named update_bars.
#
# Inside this function, calculate the new width for each bar based on the current global SCORE_A and SCORE_B variables.
#
# Use canvas.coords(bar_id, x1, y1, new_x2, y2) to redraw the bar with the new width.
#
# Hint: canvas.coords() is the most efficient way to change a shape's size/position without recreating it.
#
# Define the Button Functions:
#
# Create add_point_a() and add_point_b() functions.
#
# Inside these, increment the global score variable (SCORE_A += 1).
#
# Crucially, call update_bars() at the end of each function to refresh the visual display.

def upd_bars1():
    global score_a
    global r_1
    score_a += 1
    canvas.coords(r_1,50, 10, 50 + score_a * 2, 20)

def upd_bars2():
    global score_b
    global r_2
    score_b += 1
    canvas.coords(r_2,50,40,50 + score_b * 2,50)

# Link Buttons:
#
# Set the command option of your two buttons to add_point_a and add_point_b, respectively
#
increase_a.config(command=upd_bars1)
increase_b.config(command=upd_bars2)
window.mainloop()