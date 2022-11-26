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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text="Let's go!!!")
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
        title_label.config(text="😎 Work time 😎", fg=GREEN)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="😅 Break time 😅", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="😀 Break time 😀", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick_label.config(text="✔" * int(reps / 2))


# ---------------------------- UI SETUP ------------------------------- #

# create the window with title, padding and background color
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# create the title label
title_label = Label(text="Let's go!!!", font=(FONT_NAME, 35, "normal"), bg=YELLOW, fg=GREEN)
title_label.grid(column=2, row=0)

# create the tomato image and the timer
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=1)

# create the "Start" button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=2)

# create the tick marks
tick_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
tick_label.config(pady=20)
tick_label.grid(column=2, row=2)

# create the "Reset" button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=2)

window.mainloop()
