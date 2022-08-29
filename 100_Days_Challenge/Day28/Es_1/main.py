from cgitb import reset
import tkinter
from tkinter.tix import TEXT
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "FiraCode"
WORK_MIN = 25
WORK_SEC = 0
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WINDOW_WIDTH = 300
WINDOW_HEIGTH = 300
CHECKMARK = "✔"


# ---------------------------- TIMER RESET ------------------------------- # 

def resetALL():
    checkLabel.config(text= "")
    canvas.itemconfig(text_canvas, text=f"{WORK_MIN}:{WORK_SEC}")
    
def reset():
    canvas.itemconfig(text_canvas, text=f"{WORK_MIN}:{WORK_SEC}")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def startTimer():
    counter = 0
    countdown(WORK_MIN, WORK_SEC, counter)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(minutes, seconds, counter):
    
    canvas.itemconfig(text_canvas, text=f"{minutes}:{seconds}")
    window.after(1, countdown, minutes, seconds, counter+1)
    

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(width=WINDOW_WIDTH, height= WINDOW_HEIGTH, padx=10, pady=10, bg= YELLOW)



canvas = tkinter.Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGTH, bg=YELLOW, highlightthickness= 0)
tomatoImg = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGTH/2, image=tomatoImg)
text_canvas = canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGTH/2 +15, text=f"{WORK_MIN}:{WORK_SEC}", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column= 2)

startButton = tkinter.Button(text="Start", bg= YELLOW, activebackground= GREEN, border=0, highlightthickness= 0, command= startTimer)
startButton.grid(row=2, column=1)

resetButton = tkinter.Button(text="Reset", bg= PINK, activebackground= RED, border= 0, highlightthickness= 0, command= resetALL)
resetButton.grid(row=2, column=3)

checkLabel = tkinter.Label(text="", bg= YELLOW, fg= GREEN, font=(FONT_NAME, 28, "bold"))
checkLabel.grid(row=2, column=2)


window.mainloop()