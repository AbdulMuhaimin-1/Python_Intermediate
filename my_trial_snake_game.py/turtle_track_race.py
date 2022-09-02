from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("lightgreen")

turtle1 = Turtle(shape='turtle')
turtle1.color('red')
turtle1.speed("slow")  # = 3
turtle1.penup()

turtle2 = Turtle(shape='turtle')
turtle2.color('blue')
turtle2.speed(4)  # "slow" (3) < 4 < "normal" (6)
turtle2.penup()

# user input function

perimeter = screen.numinput("Track Perimeter", "Please enter the perimeter:", default=2000, minval=500, maxval=3000)

def full_track_crawl(turtle, shortside, longside):
    speed = turtle.speed()
    turtle.pendown()

    for j in range (2):
        for i in range(0, int(shortside), speed):
            turtle.forward(speed)
            yield(0)
        turtle.left(90)
        for i in range(0, int(longside), speed):
            turtle.forward(speed)
            yield(0)
        turtle.left(90)

    turtle.penup()

# set the track
def drawTrack(perimeter, ratio):
    shortside = (perimeter / 2.0) / (ratio + 1)
    longside = ratio * shortside

    screen.setup(shortside * 2 + 60, longside + 40)

    turtle1.setposition(-shortside - 10, -longside / 2)
    turtle2.setposition(10, -longside / 2)

    generator1 = full_track_crawl(turtle1, shortside, longside)
    generator2 = full_track_crawl(turtle2, shortside, longside)

    while (next(generator1, 1) + next(generator2, 1) < 2):
        pass

drawTrack(perimeter, 2)

screen.exitonclick()
