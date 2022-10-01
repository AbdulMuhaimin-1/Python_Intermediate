from user import User
from bank import Bank


def line():
    print("...............................")


haimin = Bank("Haimin", 24, "Male")
haimin.view_account_balance()
line()
haimin.deposit(1000)
line()
haimin.view_account_balance()
line()
haimin.deposit(500)
line()
haimin.withdrawal(600)



