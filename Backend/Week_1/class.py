class BankAccount:
    def __init__(self,name,bal):
        self.account_holder=name
        self.balance=bal
    def deposit(self,amount):
        if amount>=1:
            self.balance+=amount
        else:
            print("Incorrect amount")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient Balance")
    def display(self):
        print("Account balance : ",self.balance)

c1=BankAccount("Rishi",1000)
c2=BankAccount("Amisha",1500)

c1.deposit(500)
c1.withdraw(300)
c1.display()