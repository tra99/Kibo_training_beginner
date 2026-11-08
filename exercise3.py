class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount >0 :
            self.__balance +=amount
            print(f"Deposited {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <=0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}")

    def get_balance(self):
        return self.__balance

acc= BankAccount("Chetra", 100)

print("Owner: ", acc.owner)
print("My balance: ", acc.get_balance())

acc.deposit(50)
acc.withdraw(30)
acc.withdraw(300)