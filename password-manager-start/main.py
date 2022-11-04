from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Alert', message="Please don't leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title='SAVE', message=f"These are the details entered:\nWebsite: {website} "
                                                             f"\nEmail: {email} \nPassword: {password} "
                                                             f"\n\nIs it ok to save?")
        if is_ok:
            with open('data.txt', mode='a') as database:
                database.write(f"{website} | {email} | {password}\n")
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0, sticky='E')

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
web_entry = Entry(width=40)
web_entry.grid(column=1, row=1, columnspan=2, sticky='WE')
web_entry.focus()
email_username_entry = Entry(width=40)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky='WE')
email_username_entry.insert(0, 'yussif.muhaimin4@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='WE')

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky='W')
add_button = Button(text="Add", width=37, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='WE')



window.mainloop()
