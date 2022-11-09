from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ---------------------------------#
window = Tk()
window.title("Flash Card")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
my_image = PhotoImage(file="images/card_front.png")
canvas.create_image(405, 270, image=my_image)
language_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
dialect_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
my_right_image_button = PhotoImage(file="./images/right.png")
right_button = Button(image=my_right_image_button, highlightthickness=0)
right_button.grid(column=1, row=1)

my_wrong_image_button = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=my_wrong_image_button, highlightthickness=0)
wrong_button.grid(column=0, row=1)



window.mainloop()


