from tkinter import *
import time
import tkinter.messagebox


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


def count_down(c, tl, cm):
    global pause
    global seconds
    global checkMarkNum
    global task
    if not pause and seconds > 0:
        seconds -= 1
        window.after(1000, count_down, c, tl, cm)
    elif seconds == 0:
        if task:
            checkMarkNum += 1
            if checkMarkNum != 4:
                seconds = 300
                tl.config(text="Break", fg=PINK)
            else:
                seconds = 1200
                tl.config(text="Break", fg=RED)
            cmText = ""
            for i in range(0, checkMarkNum):
                cmText += "✔"
            cm.config(text=cmText)
            task = False
            tkinter.messagebox.showinfo("Break time")
        else:
            if checkMarkNum == 4:
                checkMarkNum = 0
                cm.config(text="")
            seconds = 1500
            tl.config(text="Work", fg=GREEN)
            task = True
            tkinter.messagebox.showinfo("Work time")
        window.after(1000, count_down, c, tl, cm)
    else:
        window.after(1, count_down, c, tl, cm)
        tl.config(text="Work", fg=GREEN)
        cm.config(text="")
    c.itemconfig(timer_text, text=time.strftime('%M:%S', time.gmtime(seconds)))


window = Tk()
window.minsize(200, 224)
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro App")


titleLabel = Label(text="Work", font=(FONT_NAME, 50, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
titleLabel.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImage)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


def start_click():
    global pause
    pause = False


startButton = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_click, highlightthickness=0)
startButton.grid(row=2, column=0)

checkMarkNum = 0
checkMarks = Label(text="", font=(FONT_NAME, 12, "normal"), bg=YELLOW, highlightthickness=0, fg=GREEN)
checkMarks.grid(row=3, column=1)

pause = True
seconds = 1500
task = True
count_down(canvas, titleLabel, checkMarks)


def reset_click():
    global seconds
    global pause
    global checkMarkNum
    global task
    seconds = 1500
    pause = True
    checkMarkNum = 0
    task = True


resetButton = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_click, highlightthickness=0)
resetButton.grid(row=2, column=2)

window.mainloop()
