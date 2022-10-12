from tkinter import *


def miles_to_km():
    km = round(float(miles_textbox.get()) * 1.609)
    km_convert_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

# Miles Textbox
miles_textbox = Entry(width=10)
miles_textbox.insert(END, string="0")
miles_textbox.grid(column=1, row=0)


# Miles Label
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# is equal to
equal_to = Label(text="is equal to", font=("Arial", 12))
equal_to.grid(column=0, row=1)
equal_to.config(padx=10, pady=10)

# Convert Textbox
km_convert_label = Label(text="0", font=("Arial", 12, "bold"))
km_convert_label.grid(column=1, row=1)

# Km Label
km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

# Button
calculate_btn = Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2)


window.mainloop()
