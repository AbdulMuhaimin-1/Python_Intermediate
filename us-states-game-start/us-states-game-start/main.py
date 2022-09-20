import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
screen.tracer(0)

df = pandas.read_csv("50_states.csv")
states = df.state.to_list()
score = 0
correct_guesses = []


while len(correct_guesses) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{score}/{len(states)} States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_guesses]
        learn_df = pandas.DataFrame(missing_states)
        learn_df.to_csv("learn.csv")
        break
    if answer_state in states:
        score += 1
        country_row = df[df.state == answer_state]
        pen.goto(int(country_row.x), int(country_row.y))
        pen.write(answer_state, font=("century gothic", 8, "bold"))
        correct_guesses.append(answer_state)

# states to learn.csv










# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

