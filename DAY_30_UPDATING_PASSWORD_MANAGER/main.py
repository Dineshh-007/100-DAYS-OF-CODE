from tkinter import *
from tkinter import messagebox
import pyperclip
import json

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
    new_data = {
        website : {
            "email" : email ,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title ="OOPS" , message= "Bruh...Don't Leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json" , "w") as data_file:
                #Saving updated data
                json.dump(data , data_file , indent= 4)

            website_input.delete(0, END)
            password_input.delete(0, END)

def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error" , message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for '{website}' found.")


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

website_input = Entry(width=18)
website_input.grid(column=1,row=1)
website_input.focus()

search = Button(text="Search" , width = 13 , command=find_password)
search.grid(column = 2 , row = 1)

email_input = Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0 , "dineshedine007@gmail.com")

password_input = Entry(width=18)
password_input.grid(column=1,row=3)

generate_button = Button(text="Generate Password",command=password_generator)
generate_button.grid(column = 2 , row = 3)

add_button = Button(text="Add",width=33 , command = save)
add_button.grid(column = 1 , row = 4 , columnspan=2)

window.mainloop()
