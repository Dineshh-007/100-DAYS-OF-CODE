import tkinter

window = tkinter.Tk()
window.minsize(500,500)

my_label = tkinter.Label(text="Hi...I'm Dinesh",font=("Aerial", 24 , "italic"))
my_label.pack(side = "left")



window.mainloop()