# Banking System using OOP
# Parent class: User
# Holds details about user

class User:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print(f"ACCOUNT DETAILS:\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}")
