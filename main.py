from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title.config(text="TIMER")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(1)
        title.config(text="WORK",fg=GREEN)
        #green
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(1)
        title.config(text="BREAK",fg=PINK)
        #pink
        #start_timer()


    elif reps == 8:
        count_down(1)
        title.config(text="BREAK",fg=RED)
        #start_timer()
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_secs = count % 60

    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_secs}")

    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)

    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


title = Label(text="TIMER",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW,highlightthickness=0)
title.grid(row=0,column=1)

check_mark = Label(bg=YELLOW,highlightthickness=0,font=(FONT_NAME,24,"bold"),fg=GREEN)
check_mark.grid(row=3,column=1)

start = Button(text="Start",command=start_timer)
reset = Button(text="Reset",command=reset_timer)
start.grid(row=2,column=0)
reset.grid(row=2,column=2)
window.mainloop()