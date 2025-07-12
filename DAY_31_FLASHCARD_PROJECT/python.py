from tkinter import *
import pandas
import random

from numpy.ma.core import filled

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient = "records")


def next_card():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title , text="French" , fill = "black")
    canvas.itemconfig(card_word , text = current_card["French"] , fill = "black")
    flip_timer = flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word , text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)

def is_correct():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()


window = Tk()
window.title("Flashy Flash Card")
window.config(padx=50 , pady=50 , bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800 , height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400 , 263 , image =card_front_img)
card_title = canvas.create_text(400,150,text="Title" , font = ("Ariel" , 40 , "italic"))
card_word = canvas.create_text(400,263 , text="word" , font = ("Ariel" , 60 , "bold"))
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
canvas.grid(row=0 , column=0 , columnspan=2)

my_cross = PhotoImage(file="images/wrong.png")
wrong_button = Button(image = my_cross , highlightthickness=0 , command=next_card)
wrong_button.grid(row = 1 , column= 0)

my_correct = PhotoImage(file="images/right.png")
correct_button = Button(image = my_correct , highlightthickness=0 , command=is_correct)
correct_button.grid(row = 1 , column = 1)

next_card()

window.mainloop()
