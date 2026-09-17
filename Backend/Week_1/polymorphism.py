class Payment:
    def pay(self,amount):
        print("Payment processing")
class UPI(Payment):
    def pay(self,amount):
        print("UPI",amount)
class CARD(Payment):
    def pay(self,amount):
        print("card",amount)
class WALLET(Payment):
    def pay(self,amount):
        print("Wallet",amount)

u=UPI()
c=CARD()
w=WALLET()
u.pay(500)
c.pay(800)
w.pay(300)