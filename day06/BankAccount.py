class BankAccount():
    total = 0

    # Constructor
    def __init__(self, account_type):
        self.account_type = account_type
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        BankAccount.total += amount

    def withdraw(self, amount):
        self.balance -= amount
        BankAccount.total -= amount

acc1 = BankAccount('savings')
acc1.deposit(15)

acc2 = BankAccount('checking')
acc2.deposit(18)

print("Total", BankAccount.total)
