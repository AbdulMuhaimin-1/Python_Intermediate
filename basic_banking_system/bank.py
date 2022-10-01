from user import User

# Child class: Bank
# Stores details about the account balance
# Stores details about the amount
# Allows for deposits, withdrawals, view_balance


class Bank(User):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def current_balance(self):
        print(f"Current Balance: Ghc{self.balance}")

    def view_account_balance(self):
        self.show_user_details()
        self.current_balance()

    def deposit(self, amount):
        self.balance += amount
        print(f"Dear {self.name}, You've received a deposit.")
        print(f"Deposit Amount: Ghc{amount}")
        self.current_balance()

    def withdrawal(self, amount):
        if self.balance < amount:
            print(f"Sorry! {self.name} You have insufficient balance in your account.\nWithdrawal Amount: {amount}")
            self.current_balance()
        else:
            self.balance -= amount
            print(f"Dear {self.name}, withdrawal was successful.")
            print(f"Account Credited: Ghc{amount}")
            self.current_balance()



