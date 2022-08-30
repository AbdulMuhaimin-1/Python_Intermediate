class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, roll_no):
        self.roll_no = roll_no

    # instance method
    def show(self):
        print("In Instance method")

    @classmethod
    def change_school(cls, name):
       print("In class method")

    @staticmethod
    def find_notes(subject_name):
        print("In Static method")


# create two objects
jessa = Student(12)
kelly = Student(25)

print(jessa.show is kelly.show)

print(jessa.find_notes is kelly.find_notes)
