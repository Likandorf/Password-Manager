from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    chosen_letters = [random.choice(letters) for char in range(randint(8, 10))]
    chosen_symbols = [random.choice(symbols) for char in range(randint(2, 4))]
    chosen_numbers = [random.choice(numbers) for char in range(randint(2, 4))]

    password_list = chosen_letters + chosen_symbols + chosen_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    website_lenght = len(website_entry.get())
    email_lenght = len(email_user_entry.get())
    password_lenght = len(password_entry.get())

    if website_lenght == 0 or email_lenght == 0 or password_lenght == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \n Is it ok to save")

        if is_ok:
            with open("my_passwords.txt", "a") as mp:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                mp.write(f"{website} | {email} | {password}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_user_entry = Entry(width=38)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "aprentis24@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
