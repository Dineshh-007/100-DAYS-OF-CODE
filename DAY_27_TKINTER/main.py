from tkinter import *

window = Tk()
window.minsize(500,300)
window.config(padx=20 ,pady=20)

def button_clicked():
    my_label["text"] = "New text"
    new_text = input.get()
    my_label.config(text=new_text)


my_label = Label(text="Hi...I'm Dinesh",font=("Aerial", 24 , "italic"))

my_label["text"] = "New text"
my_label.config(text="New text")
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click me",command=button_clicked)
button.grid(column=1, row=1)

#New Button
new_button = Button(text="Click me,bruh")
new_button.grid(column=2, row=0)

# #Entry
input = Entry(width=10)
input.grid(column=3,row=3)





window.mainloop()