class Atm():
    def __init__(self,card_no,pin_no):
        self.card_no=card_no
        self.pin_no=pin_no

    def cashWithdraw(self,amount):
        newAmount=50000-amount
        print("Your remaining balance is"+str(newAmount))

    def balanceEnquiry(self):
        print("Your balance is 50000")

def main():
    card_no=input("Enter your card number")
    pin_no=input("Enter your pin number")
    newUser=Atm(card_no,pin_no)
    newUser.balanceEnquiry()
    newUser.cashWithdraw(500)
main()