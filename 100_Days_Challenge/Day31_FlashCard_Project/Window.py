from email.mime import image
import tkinter
from Data_Creation import DataScraper

cardsData = DataScraper()
BACKGROUND_COLOR = "#B1DDC6"
PADDING_X = 50
PADDING_Y = 50
FONT_TITLE = ("Verdana", 40, "italic")
FONT_WORD = ("Verdana", 60, "bold")
FONT_WHITE = "white"
FONT_BLACK = "black"
WINDOW_WIDTH = 300
WINDOW_HEIGTH = 300
CANVAS_WIDTH = 800
CANVAS_HEIGTH = 526

# cardBackImg = tkinter.PhotoImage(file= "./images/card_back.png")


class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flashy")
        self.config(padx=PADDING_X, pady=PADDING_Y, bg=BACKGROUND_COLOR)

        self.cardFrontImg = tkinter.PhotoImage(file="./images/card_front.png")
        self.cardBackImg = tkinter.PhotoImage(file="./images/card_back.png")
        
        self.fliptimer = self.after(ms = 3000, func=self.flipCard)
        self.newCard()

        self.initRightBtn()
        self.initWrongBtn()

    def initCanvas(self):
        self.canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGTH,
                                     bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvasBG = self.canvas.create_image(
            CANVAS_WIDTH/2, CANVAS_HEIGTH/2, image=self.cardFrontImg)
        self.canvas.grid(row=0, column=0, columnspan=2)

    def initFlashText(self):
        self.cardTitle = self.canvas.create_text(CANVAS_WIDTH/2, 150,
                                                 text="Title", font=FONT_TITLE, fill= FONT_BLACK)
        self.cardWord = self.canvas.create_text(
            CANVAS_WIDTH/2, CANVAS_HEIGTH/2, text="word", font=FONT_WORD, fill= FONT_BLACK)

    def initRightBtn(self):
        # Add the right button to the window
        self.rightBtnImg = tkinter.PhotoImage(file="./images/right.png")
        self.rightBtn = tkinter.Button(
            image=self.rightBtnImg, borderwidth=0, highlightthickness=0, command=self.removeWord)
        self.rightBtn.grid(row=1, column=1)

    def initWrongBtn(self):
        # Add the wrong button to the window
        self.wrongBtnImg = tkinter.PhotoImage(file="./images/wrong.png")
        self.wrongBtn = tkinter.Button(
            image=self.wrongBtnImg, borderwidth=0, highlightthickness=0, command=self.newCard)
        self.wrongBtn.grid(row=1, column=0)

    def newCard(self):
        
        self.initCanvas()
        self.initFlashText()
    
        
        if len(cardsData.toLearn)>1:
            self.after_cancel(self.fliptimer)
            self.card_to_show = cardsData.next_card()
            self.canvas.itemconfig(self.cardTitle, text="French")
            self.canvas.itemconfig(self.cardWord, text=self.card_to_show["French"])
            self.fliptimer = self.after(ms = 3000, func=self.flipCard)
        else:
            self.cardsFinished()
            
    def flipCard(self):
        self.canvas.itemconfig(self.canvasBG, image= self.cardBackImg)
        self.canvas.itemconfig(self.cardTitle, text="English", fill= FONT_WHITE)
        self.canvas.itemconfig(self.cardWord, text=self.card_to_show["English"], fill= FONT_WHITE) 
        
    def removeWord(self):
        
        if len(cardsData.toLearn) > 1:
            cardsData.toLearn.remove(self.card_to_show)
            cardsData.saveNotLearned()
            self.newCard()
        else:
            self.cardsFinished()
    
    
    def cardsFinished(self):
        try:
            cardsData.toLearn.remove(self.card_to_show)
            cardsData.saveNotLearned()
        except:
            pass
        else:        
            self.initCanvas()
            self.initFlashText()

            self.after_cancel(self.fliptimer)

            self.canvas.itemconfig(self.cardTitle, text="Congratulations!")
            self.canvas.itemconfig(self.cardWord, text="You Learned \nall the words")