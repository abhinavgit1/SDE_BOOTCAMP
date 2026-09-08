class User:
    def __init__(self,nname,eemail):
        self.name=nname
        self.email=eemail
    def login(self):
        print("Login Successfull",self.name)
class Customer(User):
    def __init__(self,bal,nname,eemail):
        User.__init__(self,nname,eemail)
        self.balance=bal
    def show_balance(self):
        print(self.balance)
c1=Customer(2000,"Raju","abc@gmail.com")
c1.show_balance()
c1.login()

