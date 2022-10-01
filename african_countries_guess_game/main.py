import turtle

screen = turtle.Screen()
img = "africa_map.gif"
screen.addshape(img)
turtle.shape(img)

countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central",
             "African Republic (CAR)", "Chad", "Comoros", "Democratic Republic of the Congo",
             "Republic of the Congo, Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini",
             "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya",
             "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger",
             "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia",
             "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
x = []
y = []

# answer = screen.textinput(title="Guess The Turtle", prompt="Enter the country to be guessed:")


def get_coordinates(x_cor, y_cor):
    print(f"X = {x_cor}, Y = {y_cor}")


turtle.onscreenclick(get_coordinates)


screen.mainloop()



