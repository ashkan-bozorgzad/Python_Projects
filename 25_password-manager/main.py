from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
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
def save_pass():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please do not leave ant fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Load old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update the old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_pass():
    user_website = website_entry.get()
    if user_website:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="Empty Database", message="No password has been saved")
        else:
            if user_website in data:
                username = data[user_website]["username"]
                password = data[user_website]["password"]
                messagebox.showinfo(title=user_website, message=f"Username: {username}\n Password: {password}")
            else:
                messagebox.showwarning(title="Not found", message="There is no password for this website")
    else:
        messagebox.showwarning(title="Empty field", message="PLease fill the website")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "abc@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons

# calls generate_pass() when pressed
generate_pass_button = Button(text="Generate Password", command=generate_pass)
generate_pass_button.grid(column=2, row=3)

# calls save_pass() when pressed
add_button = Button(text="Add", width=43, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

# calls save_pass() when pressed
search_button = Button(text="search", width=14, command=find_pass)
search_button.grid(column=2, row=1)

window.mainloop()
