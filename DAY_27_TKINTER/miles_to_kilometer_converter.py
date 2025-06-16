from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")

def calculate_clicked():
    mile = float(miles_input.get())
    kilometer = mile * 1.609
    km_con.config(text=kilometer)



miles_input = Entry()
miles_input.grid(column=10,row=10)

miles = Label(text="miles",font=("Aerial", 24 , "italic"))
miles.grid(column=20,row=10)

km_con = Label(text="0",font=("Aerial", 24 , "italic"))
km_con.grid(column=10,row=20)

calculate = Button(text="Calculate",command=calculate_clicked)
calculate.grid(column=10,row=30)

is_equal_to = Label(text="is equal to",font=("Aerial", 24 , "italic"))
is_equal_to.grid(column=0,row=20)

km = Label(text="km",font=("Aerial", 24 , "italic"))
km.grid(column=20,row=20)


window.mainloop()