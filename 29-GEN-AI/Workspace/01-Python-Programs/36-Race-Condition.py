import threading
import time

balance = 1000

lock = threading.Lock()


def withdraw(amount):
    global balance
    with lock:
        if balance >= amount:
            current_balance = balance
            time.sleep(1)
            balance = current_balance - amount
            print("Withdraw success....", threading.current_thread().name)
            print("Remaining Balance : ", balance)
        else:
            print("Insufficient funds : ",  threading.current_thread().name)


t1 = threading.Thread(target=withdraw, args=(700,))
t2 = threading.Thread(target=withdraw, args=(700,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balance :", balance)