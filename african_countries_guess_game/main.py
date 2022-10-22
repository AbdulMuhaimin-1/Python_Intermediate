import turtle
import pandas

screen = turtle.Screen()
img = "africa_map.gif"
screen.addshape(img)
turtle.shape(img)

country_df = pandas.read_csv("country_coord.csv")
print(country_df.loc[3])

answer = screen.textinput(title="Guess The Turtle", prompt="Enter the country to be guessed:")




screen.mainloop()



