
from tkinter import *
import turtle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50, bg="black")

canvas = Canvas(height=300, width=300, bg="black", highlightthickness=0)
photo = PhotoImage(file="./logo.png")
canvas.create_image(200, 200, image=photo)
canvas.grid(column=0, row=0)

window.mainloop()
