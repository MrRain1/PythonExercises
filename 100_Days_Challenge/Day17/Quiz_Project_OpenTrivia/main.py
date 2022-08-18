from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

def printQuestionBank():
    for index in range(len(question_bank)):
        print(question_bank[index].text)

def initializeQuestionBank():
    for question in question_data:
        question_bank.append(Question(question["question"], question["correct_answer"]))

initializeQuestionBank()

quiz = QuizBrain(question_bank)

while(quiz.stillHasQuestions()):
    quiz.next_question()

quiz.printFinalScore()