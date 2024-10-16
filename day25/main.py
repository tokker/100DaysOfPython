import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(700, 500)


data = pandas.read_csv("50_states.csv")
state_names = data["state"].tolist()
states_guessed_cnt = 0
guessed_states = []
turtle.hideturtle()
turtle.penup()

while states_guessed_cnt < 50:
    answer = screen.textinput(str(states_guessed_cnt) + "/50 States Correct", "What's another state's name")
    for state in state_names:
        if answer.lower() == state.lower() and state not in guessed_states:
            states_guessed_cnt += 1
            xcor = data[data.state == state].x.item()
            ycor = data[data.state == state].y.item()
            turtle.goto(xcor, ycor)
            turtle.write(state, False)
            guessed_states.append(state)

turtle.goto(0, 0)
turtle.write("Congratulations, you guessed all the 50 states!", False, "center", ("Arial", 20, "bold"))

screen.exitonclick()
