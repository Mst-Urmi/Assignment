class BankAccount:
    def __init__(self, starting_balance):
        self.__balance = starting_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

# Sample Input
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(300)
print(account.get_balance())  # Output: 1200
account.withdraw(1500)        # Output: Insufficient funds!
