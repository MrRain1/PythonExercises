import turtle
import pandas

state_data = pandas.read_csv("./50_states.csv")
state_names = state_data["state"].to_list()
already_answered = []


screen = turtle.Screen()
screen.bgpic("./blank_states_img.gif")
screen.title("U.S. States Game")

turt = turtle.Turtle()
turt.hideturtle()

gameState = True

def exitGame():
    return False

def writeStateName(answer):
    x_coor = int(state_data[state_data["state"] == answer].x)
    y_coor = int(state_data[state_data["state"] == answer].y)
    turt.penup()
    turt.goto(x= x_coor, y= y_coor)
    turt.pendown()
    turt.write(arg= answer, align="Center", font=["Arial", 8, "bold"])

while(gameState):
    answer_state = screen.textinput(title="Guess a State Name", prompt="Insert a valid State name")
    if answer_state is not None:
        answer_state = answer_state.title()

    if((answer_state in state_names) and (answer_state not in already_answered)):
        writeStateName(answer_state)
        already_answered.append(answer_state)
        
    if ((answer_state is None) or (len(already_answered) == 50)):
        gameState = exitGame()
        missing_states = [state for state in state_names if state not in already_answered]
        pandas.DataFrame(missing_states).to_csv("./states_to_learn.csv")

screen.mainloop()