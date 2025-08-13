#Wrapping data and method into a single unit is called encapsulation.

# Explanation :
# __balance is private (Direct access not allowed) → આ encapsulation છે, dataને hide કરવું.
# deposit(), withdraw(), અને get_balance() methods વડે જ data access કરી શકાય છે.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable (encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Using the class
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # 1300
