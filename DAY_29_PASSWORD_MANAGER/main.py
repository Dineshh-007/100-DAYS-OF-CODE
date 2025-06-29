from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]

    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]

    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0 , f"{password}")

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title ="OOPS" , message= "Bruh...Don't Leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="Information" , message=f"The details that you entered are:\n "
                                                             f"Website : {website}\n"
                                                             f"Email : {email}\n"
                                                             f"Password: {password}\n"
                                                                     f"Is it ok to save?" )
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}  ||  {email}  ||  {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50 , pady=50)

canvas = Canvas(width=200 , height=200 , highlightthickness = 0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100 , 100 , image =logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0 , row=1)

email = Label(text="Email / Username :")
email.grid(column=0 , row=2)

password = Label(text="Password:")
password.grid(column=0 , row=3)

website_input = Entry(width=35)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0 , "@gmail.com")

password_input = Entry(width=18)
password_input.grid(column=1,row=3)

generate_button = Button(text="Generate Password",command=password_generator)
generate_button.grid(column = 2 , row = 3)

add_button = Button(text="Add",width=33 , command = save)
add_button.grid(column = 1 , row = 4 , columnspan=2)



window.mainloop()
