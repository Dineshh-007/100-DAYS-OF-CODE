from tkinter import *

window = Tk()
window.minsize(500,500)

my_label = Label(text="Hi...I'm Dinesh",font=("Aerial", 24 , "italic"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="New text")

def button_clicked():
    my_label["text"] = "New text"
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got clicked...")

#Buttons
button = Button(text="Click me",command=button_clicked)
button.pack()

# #Entry

input = Entry(width=10)
input.pack()




window.mainloop()