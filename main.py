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
started = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label.config(text='Timer')
    checmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_countdown():
    short_break = SHORT_BREAK_MIN * 60
    work = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break)
        label.config(text="Start a long break", fg=RED)
    if reps % 2 == 0:
        count_down(short_break)
        label.config(text="Break", fg=PINK)
    elif reps % 2 == 1:
        count_down(work)
        label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        timer = windows.after(10, count_down, count - 1)
    else:
        if reps < 9:
            start_countdown()
        marks = ""
        a = math.floor(reps / 2)
        for i in range(a):
            marks += '✔'
        checmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title('Pomodoro')
windows.config(padx=100, pady=50)
canvas = Canvas(width=200, height=224, highlightthickness=0)
windows["bg"] = YELLOW

# tomato

tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(103, 112, image=tomato_image)
canvas["bg"] = YELLOW
canvas.grid(row=1, column=1)
# canvas.pack()
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 20, 'bold'))

# text

label = Label(text='Timer', font=(FONT_NAME, 44, 'bold'))
# label.grid(row=0, column=0)
# label.pack(expand=True, ipadx=10, ipady=10)
label.grid(row=0, column=1)
label.configure(fg=GREEN, bg=YELLOW)

# Button
btn = Button(text='start', command=start_countdown, font=(FONT_NAME, 10))
btn.grid(row=2, column=0)
# btn.pack(side=LEFT)
btn_2 = Button(text='reset', command=reset_timer, font=(FONT_NAME, 10))
btn_2.grid(row=2, column=2)
# btn.pack(side=RIGHT)

checmark_label = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
checmark_label.grid(row=3, column=1)

windows.mainloop()
