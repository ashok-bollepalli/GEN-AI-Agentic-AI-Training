from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    def payment_success(self):
        print("Payment is successfull...")


class UpiPayment(Payment):
    def pay(self, amount):
        print("Paid using UPI : ", amount)
        super().payment_success()

class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid using CreditCard :", amount)
        super().payment_success()


payment_type = UpiPayment()
payment_type.pay(100)


payment_type = CreditCardPayment()
payment_type.pay(200)