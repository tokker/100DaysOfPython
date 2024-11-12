from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Manager")


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logoImage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImage)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 10, "normal"), bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("Arial", 10, "normal"), bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Arial", 10, "normal"), bg="white")
password_label.grid(row=3, column=0)

website_input = Entry(width=55)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=55)
email_input.insert(0, "td00@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=36)
password_input.grid(row=3, column=1)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = [random.choice(letters) for _ in range(random.randint(8, 10))] + [random.choice(numbers) for _ in range(random.randint(2, 4))] + [random.choice(symbols) for _ in range(random.randint(2, 4))]
    random.shuffle(password)
    password_input.delete(0, END)
    password_input.insert(0, "".join(password))
    pyperclip.copy("".join(password))



generate_button = Button(text="Generate Password", command=generate_password, width=15)
generate_button.grid(row=3, column=2)


def add_password():
    if website_input.get() != "" and email_input.get() != "" and password_input.get() != "":
        is_ok = messagebox.askokcancel(website_input.get(),
                               f"These are the details entered:\nEmail: {email_input.get()}\nPassword: {password_input.get()}\nIs it OK to save?")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            messagebox.showinfo("Password saved", "You successfully saved a password.")
    elif website_input.get() == "":
        messagebox.showinfo("Empty website", "Please enter the name of the website.")
    elif email_input.get() == "":
        messagebox.showinfo("Empty email/username", "Please enter your email or username.")
    elif password_input.get() == "":
        messagebox.showinfo("Empty password", "Please enter the password.")

add_button = Button(text="Add", command=add_password, width=47)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
