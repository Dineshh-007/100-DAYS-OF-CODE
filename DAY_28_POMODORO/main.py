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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text , text= "00:00")
    title.config(text="TIMER")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        title.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="WORK", fg=YELLOW)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count <= 9:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text , text = f"{min_count}:{sec_count}")
    if count > 0 :
        global timer
        timer = window.after(1000 , count_down , count-1)
    else:
        start_timer()
        # ✅
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks+= "✅"
        check_mark.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100 , pady=50 ,bg = GREEN)

title = Label(text="TIMER" , fg = RED , bg=GREEN,font=(FONT_NAME, 35 ))
title.grid(column=1 , row=0)


canvas = Canvas(width=200 , height=224 , bg = GREEN , highlightthickness = 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100 , 112 , image = tomato_img)
timer_text = canvas.create_text(100,130 ,text = "00:00",fill = "white", font=(FONT_NAME, 35 , "bold"))
canvas.grid(column=1, row=1)



start_button = Button(text="START" , bg= GREEN , highlightthickness= 0, command=start_timer)
start_button.grid(column=0 , row =2)

reset_button = Button(text="RESET", bg = GREEN , highlightthickness= 0, command=reset_timer)
reset_button.grid(column=2 , row =2)

#  ✅
check_mark = Label(fg = PINK , bg = GREEN)
check_mark.grid(column=1 , row =3)

window.mainloop()