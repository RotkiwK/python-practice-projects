class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.owner, "deposited", amount, "- balance is now", self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print(self.owner,"- insufficient founds")
        else:
            self.balance = self.balance - amount
            print (self.owner, "withdraw", amount, "- balance is now", self.balance)

    def show_balance(self):
        print (self.owner, "has ",self.balance)

wiktor = BankAccount("Wiktor")
wiktor.deposit(100)
wiktor.withdraw(30)
wiktor.withdraw(500)     # should hit insufficient funds
wiktor.show_balance()

oskar = BankAccount("Oskar")
oskar.deposit(50)
oskar.withdraw(0)
oskar.show_balance()

