import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# lable

my_label = tkinter.Label(text="I'm a label", font=("FiraCode", 24, "italic"))
my_label.pack()


window.mainloop()