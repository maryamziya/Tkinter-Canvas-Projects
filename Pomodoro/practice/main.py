
# # Instructions ⏰
# # Setup & Initial Canvas Text:
# #
# # Create the main window and a Canvas widget. Make the canvas large enough to hold a clock face (e.g., 300x100).
from tkinter import *
from datetime import datetime
window = Tk()
window.config(width=1000,height=1000)
canvas = Canvas(width=800,height=600)
img = PhotoImage(file="clock.png")
canvas.create_image(400,300,image=img)
# # Use canvas.create_text() to place the initial time text (e.g., "00:00:00") in the center of the canvas. Store the returned ID (clock_text_id).
clock_text_id = canvas.create_text(400,300,text="00:00:00",fill="#B99C81",font=("Courier",75,"bold"))
canvas.pack()


# # Get Real Time:
# #
# # Import the time module (import time).
# #



# # Define a function, perhaps named update_time(), that retrieves the current time formatted as a string (e.g., "HH:MM:SS").
def upd_time():
    now = datetime.now()
# # Hint: You can use time.strftime("%H:%M:%S").
    current_time_string = now.strftime("%I:%M:%S")
# # Update the Canvas:
# #
# # Inside the update_time() function, use canvas.itemconfig(clock_text_id, text=current_time_string) to update the display.
    canvas.itemconfig(clock_text_id,text = current_time_string)
# # Continuous Loop:

# # Crucially, use the window.after(1000, update_time) method inside the update_time function itself to create a loop that calls the function every 1000 milliseconds (1 second).
    window.after(1000,upd_time)
# # Call update_time() once outside the function to start the loop.
upd_time()
# # Optional Graphical Element (Image/Shape):
# #
# # Add a simple decorative element to the canvas using either canvas.create_rectangle() or canvas.create_oval() to act as a frame around the time text, or use PhotoImage to load a simple clock image.


# #
# # Hint: Place this graphic before the text, so the text is rendered on top.

window.mainloop()