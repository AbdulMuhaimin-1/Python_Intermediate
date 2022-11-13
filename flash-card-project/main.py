from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------GENERATE WORDS -----------------------------#
df = pandas.read_csv('data/french_words.csv')
word_dict = [{row.French: row.English} for (index, row) in df.iterrows()]


def random_word():
    french_word = random.choice(word_dict)
    return french_word


def generate_words():
    canvas.itemconfig(dialect_text, text=[key for key in random_word().keys()][0])
    canvas.itemconfig(language_text, text="French", font=("Arial", 40, "italic"))


# ---------------------------- UI SETUP ---------------------------------#
window = Tk()
window.title("Flash Card")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
my_image = PhotoImage(file="images/card_front.png")
canvas.create_image(405, 270, image=my_image)
language_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
dialect_text = canvas.create_text(400, 263, text=[key for key in random_word().keys()][0], font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
my_right_image_button = PhotoImage(file="./images/right.png")
right_button = Button(image=my_right_image_button, highlightthickness=0, command=generate_words)
right_button.grid(column=1, row=1)

my_wrong_image_button = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=my_wrong_image_button, highlightthickness=0, command=generate_words)
wrong_button.grid(column=0, row=1)


window.mainloop()


