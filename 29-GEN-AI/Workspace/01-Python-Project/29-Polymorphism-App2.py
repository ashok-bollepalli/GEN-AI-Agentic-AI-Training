class UpiPayment:
    def pay(self, amount):
        print(f"paid {amount} using UPI")
#-----------------------------------------------#
class CreditCardPayment:
    def pay(self, amount):
        print(f"paid {amount} using CreditCard")
#-----------------------------------------------#
class DebitCardPayment:
    def pay(self, amount):
        print(f"paid {amount} using DebitCard")
#-----------------------------------------------#
def make_payment(payment_type, amount):
    payment_type.pay(amount)
#-----------------------------------------------#
make_payment(CreditCardPayment(), 1000)
make_payment(DebitCardPayment(), 2000)
make_payment(UpiPayment(), 10000)


