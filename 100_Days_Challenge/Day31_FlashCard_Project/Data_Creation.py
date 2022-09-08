import pandas
import random


class DataScraper():
    def __init__(self):

        try:
            self.data = pandas.read_csv("./data/words_to_learn.csv")
            
            if self.data.empty:
                print("DB is empty!")
                self.data = pandas.read_csv("./data/french_words.csv")
            
            # print("Loaded words_to_learn")
        except FileNotFoundError:
            self.data = pandas.read_csv("./data/french_words.csv")
            # print("No file found, reading from complete db")
        finally:
            self.toLearn = self.data.to_dict(orient="records")

    def next_card(self):
        self.currentCard = random.choice(self.toLearn)
        return self.currentCard

    def saveNotLearned(self):
        data = pandas.DataFrame(self.toLearn)
        data.to_csv("./data/words_to_learn.csv")
