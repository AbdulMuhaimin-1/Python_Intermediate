from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# ------------------------------GENERATE WORDS -----------------------------#
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def generate_words():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(dialect_text, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(dialect_text, text=current_card['English'], fill='white')


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    new_list = pandas.DataFrame(to_learn)
    new_list.to_csv('data/words_to_learn.csv', index=False)
    generate_words()


# ---------------------------- UI SETUP ---------------------------------#
window = Tk()
window.title("Flash Card")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(405, 270, image=card_front_image)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
dialect_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
my_right_image_button = PhotoImage(file="./images/right.png")
right_button = Button(image=my_right_image_button, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

my_wrong_image_button = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=my_wrong_image_button, highlightthickness=0, command=generate_words)
wrong_button.grid(column=0, row=1)

generate_words()
window.mainloop()


