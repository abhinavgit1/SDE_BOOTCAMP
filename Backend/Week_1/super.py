class User:
    def __init__(self,nname,eemail):
        self.name=nname
        self.email=eemail
    def login(self):
        print("Login Successfull",self.name)
class Customer(User):
    def __init__(self,bal,nname,eemail):
        super().__init__(nname,eemail)
        self.balance=bal
    def show_balance(self):
        print(self.balance)
c1=Customer(2000,"Raju","abc@gmail.com")
c1.show_balance()
c1.login()


class Vehicle:
    def start(self):
        print("Engine Started")
class Bike(Vehicle):
    def start(self):
        print("Bike Started")
class Car(Vehicle):
    def start(self):
        print("Car Started")
v=Vehicle()
b=Bike()
c=Car()
v.start()
b.start()
c.start()
