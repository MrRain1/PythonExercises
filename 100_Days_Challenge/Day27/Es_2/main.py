from time import sleep
import tkinter


def changeText():
    label.config(text=text.get())

window = tkinter.Tk()
window.title("Changing lable with button")
window.minsize(width=500, height=300)

label = tkinter.Label(text="Not Clicked", font=("FiraCode", 12))
label.pack()

button = tkinter.Button(text="Click me!", command= changeText)
button.pack()

#Eentry

text= tkinter.Entry()
text.pack()
window.mainloop()