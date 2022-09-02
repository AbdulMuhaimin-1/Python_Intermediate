import turtle as t


screen = t.Screen()
screen.setup(600, 500)
is_snake_alive = True
x_pos = [0, 8, 16]
movement = [100, 108, 116]
snake = []


# tim = t.Turtle(shape="square")
# tim.stamp()
# tim.forward(30)

for turtle_snake in range(3):
    new_snake = t.Turtle(shape="square")
    new_snake.goto(x=x_pos[turtle_snake], y=0)
    snake.append(new_snake)


while is_snake_alive:
    for snakes in snake:
        snakes.forward(30)
        snakes.right(90)



screen.exitonclick()
