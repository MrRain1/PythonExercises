import tkinter

def calculateMiles():
    conversion_result = "0"
    
    if textbox.get() != "":
        conversion_result = str(round(float(textbox.get())/1.609, 2))
    
    outputLabel.config(text= conversion_result)        
    

window = tkinter.Tk()
window.config(width= 300 , height=200, padx= 10, pady= 10)
window.title("Km to Mile converter")

textbox = tkinter.Entry(width= 10, justify= "center")
textbox.grid(column= 2, row= 1)
kmLabel = tkinter.Label(text="Km")
kmLabel.grid(column= 3, row= 1)

textPiece1 = tkinter.Label(text="is equal to:")
textPiece1.grid(column= 1, row= 2)

outputLabel = tkinter.Label(text="0", pady= 10)
outputLabel.grid(column= 2, row= 2)

milesLabel = tkinter.Label(text="Miles")
milesLabel.grid(column=3, row=2)

calcButton = tkinter.Button(text="Calculate", command=calculateMiles)
calcButton.grid(column=2, row= 3)

window.mainloop()

