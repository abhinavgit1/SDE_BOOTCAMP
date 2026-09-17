class BankAccount:

    def __init__(self,bal):
        self.__balance=bal

    def deposit(self,amount):
        if amount<=0:
            print("Amount must be positive")
        else:
            self.__balance+=amount

    def withdraw(self,amount):
        bal=self.__balance
        if amount>bal:
            print("Low balance")
        else:
            self.__balance-=amount

    def get_balance(self):
        print("Balance is : ",self.__balance)

bb=BankAccount(1500)

bb.get_balance()
bb.deposit(500)
bb.withdraw(1000)
bb.get_balance()

