import tkinter
from random import randint
from tkinter import messagebox
import json

WINDOW_WIDTH = 300
WINDOW_HEIGTH = 300
CANVAS_WIDTH = 200
CANVAS_HEIGTH = 200
PADDING = 20
FONT_NAME = ("Verdana", 10)
PADDING_BETWEEN = 5
NR_LETTERS = 7
NR_SYMBOLS = 2
NR_NUMBERS = 3

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generatePass():
    initPass = []
    for countLetters in range(1, NR_LETTERS+1):
        initPass.append(letters[randint(0, len(letters)-1)])

    for countSymbols in range(1, NR_SYMBOLS+1):
        initPass.append(symbols[randint(0, len(symbols)-1)])

    for countNumbers in range(1, NR_NUMBERS+1):
        initPass.append(numbers[randint(0, len(numbers)-1)])

    hardPass = []

    for length in range(-1, len(initPass) - 1):
        rand = randint(0, len(initPass) - 1)
        hardPass.append(initPass[rand])
        initPass.remove(initPass[rand])

    pswInput.delete(first=0, last=tkinter.END)
    pswInput.insert(0, "".join(hardPass))

# ---------------------------- SAVE PASSWORD ------------------------------- #


def saveAccount():

    website = urlInput.get()
    username = usrInput.get()
    password = pswInput.get()

    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    response = messagebox.askokcancel(
        title="Proceed Registration", message=f"These are the details entered:\nEmail/Username: {username}\nPassword: {password}\nIs it ok to save?")

    if response:

        if website == "":
            messagebox.showerror(title="Invalid Website",
                                 message="Website cannot be blank")
            return

        if username == "":
            messagebox.showerror(title="Invalid Email/Username",
                                 message="Email/Username cannt be blank")
            return

        if password == "":
            messagebox.showerror(title="Invalid Password",
                                 message="Password cannt be blank")
            return

        try:
            with open("./passwords.json", "r") as document:
                data = json.load(document)
        except FileNotFoundError:
            writeData(new_data)
        else:
            data.update(new_data)
            writeData(data)
        finally:
            urlInput.delete(0, tkinter.END)
            usrInput.delete(0, tkinter.END)
            pswInput.delete(0, tkinter.END)

    messagebox.showinfo(title="Success", message="Registration Successful")


def writeData(data_to_write):
    with open("./passwords.json", "w") as document_to_write:
        json.dump(data_to_write, document_to_write, indent=4)


# Find Data

def queryData():

    website = urlInput.get()

    if website != "":
        try:
            with open("./passwords.json", "r") as database:
                data = json.load(database)
        except FileNotFoundError:
            messagebox.showerror(title="No Data",
                                 message="You didn't add anything to the database yet")
            return
        else:
            if website in data:
                messagebox.showinfo(
                    title="Found Match", message=f"These are the details entered:\nEmail/Username: \n{data[website]['email']}\nPassword: \n{data[website]['password']}")
            else:
                messagebox.showerror(
                    title="No Matches", message="No matches found in the database")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(width=WINDOW_WIDTH, height=WINDOW_HEIGTH,
              padx=PADDING+30, pady=PADDING, bg="white")

canvas = tkinter.Canvas(
    width=CANVAS_WIDTH, height=CANVAS_HEIGTH, bg="white", highlightthickness=0)
lockImg = tkinter.PhotoImage(file="./logo.png")
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGTH/2, image=lockImg)
canvas.grid(row=0, column=1)

websiteLabel = tkinter.Label(
    text="Website:", background="white", font=FONT_NAME)
websiteLabel.grid(row=1, column=0)

urlInput = tkinter.Entry(width=21, font=FONT_NAME)
urlInput.grid(row=1, column=1, pady=PADDING_BETWEEN)

searchButton = tkinter.Button(
    text="Search", background="white", font=FONT_NAME, command= queryData)
searchButton.grid(row=1, column=2, pady=PADDING_BETWEEN)


urlInput.focus()

usrLable = tkinter.Label(text="Email/Username:",
                         background="white", font=FONT_NAME)
usrLable.grid(row=2, column=0)

usrInput = tkinter.Entry(width=35, font=FONT_NAME)
usrInput.grid(row=2, column=1, columnspan=2, pady=PADDING_BETWEEN)

pswLabel = tkinter.Label(text="Password:", bg="white", font=FONT_NAME)
pswLabel.grid(row=3, column=0)

pswInput = tkinter.Entry(width=21, font=FONT_NAME, )
pswInput.grid(row=3, column=1, pady=PADDING_BETWEEN)

randomPass = tkinter.Button(
    text="Generate Password", background="white", font=FONT_NAME, command=generatePass)
randomPass.grid(row=3, column=2, pady=PADDING_BETWEEN)

addEntryBtn = tkinter.Button(
    text="Add", background="white", width=36,  font=FONT_NAME, command=saveAccount)
addEntryBtn.grid(row=4, column=1, columnspan=2, pady=PADDING_BETWEEN)

window.mainloop()
