from tkinter import messagebox
import random
from tkinter import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    entry_pw.insert(0, password)
    pyperclip.copy(password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    text = f"{entry_website.get()} | {entry_mail.get()} | {entry_pw.get()}\n"

    if len(entry_website.get()) == 0 or len(entry_pw.get()) == 0 or len(entry_mail.get()) == 0:
        messagebox.showinfo(title="Error", message="please dont leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=entry_website.get(), message=f'{entry_mail.get()}\n{entry_pw.get()}'
                                                                          f'\nsave this information to you '
                                                                          f'list of passwords?'
                                                                          f'\nNote, the new password has been copied '
                                                                          f'to your clipboard.')

        if is_ok:
            with open("./passwords.txt", "a") as passwords:
                passwords.write(text)
            entry_pw.delete(0, END)
            entry_mail.delete(0, END)
            entry_website.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
photo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

label_web = Label(text="Website:", highlightthickness=0, bg="white")
label_web.grid(column=0, row=1)

label_email = Label(text="Email/Username::", highlightthickness=0, bg="white")
label_email.grid(column=0, row=2)

label_pw = Label(text="Password:", highlightthickness=0, bg="white")
label_pw.grid(column=0, row=3)

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_mail = Entry(width=35)
entry_mail.grid(column=1, row=2, columnspan=2)
entry_mail.insert(0, "tobifakemail@gmail.com")

entry_pw = Entry(width=21)
entry_pw.grid(column=1, row=3)

button_generate_pw = Button(text="Generate Password", command=generate_password)
button_generate_pw.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

print(entry_mail.get())
window.mainloop()
