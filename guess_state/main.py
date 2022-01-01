import turtle
import pandas

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
guessed_state = []

screen = turtle.Screen()
screen.title("US State Guess")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)} states guessed",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_state]
        to_learn = pandas.DataFrame(missing_states)
        to_learn.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        desired_state = data[data.state == answer_state]
        t.goto(int(desired_state.x), int(desired_state.y))
        t.write(answer_state)


