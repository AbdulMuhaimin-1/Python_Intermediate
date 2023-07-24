import turtle
import pandas

countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Cabo Verde", "Cameroon",
             "Central African Republic", "Chad", "Comoros", "Democratic Republic of the Congo", "Republic of the Congo",
             "Cote d'Ivoire", "Djibouti", "Egypt", "Eritrea", "Ethiopia", "Gabon", "Ghana", "Guinea", "Guinea-Bissau",
             "Kenya", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Morocco", "Mozambique",
             "Namibia", "Niger", "Nigeria", "Senegal", "Sierra Leone", "Somalia", "South Africa", "South Sudan",
             "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

x = [-128, -10, -99, 30, -138, -277, -45, -3, -4, 185, 3, -14, -161, 171, 62, 138, 129, -46, 127, -200, -212, 130, -181,
     -19, 186, 113, -145, -209, -159, 113, -20, -62, -76, -218, -194, 199, 16, 69, 59, 92, -105, -53, 94, 45, 67]

y = [202, -82, 71, -163, 83, 130, 36, 40, 118, -96, -35, -7, 45, 81, 192, 109, 58, -9, 43, 73, 82, 8, 49, 200, -135,
     -102, 129, 143, 229, -134, -147, 126, 70, 104, 57, 63, -245, 53, 119, 47, 59, 241, 2, -108, -144]

countries_dict = {
    "Country": countries,
    "X_Coord": x,
    "Y_Coord": y,
}

countries_df = pandas.DataFrame(countries_dict)
countries_df.to_csv("country_coord.csv")


def get_coordinates(x_cor, y_cor):
    print(f"X = {x_cor}, Y = {y_cor}")
turtle.onscreenclick(get_coordinates)
