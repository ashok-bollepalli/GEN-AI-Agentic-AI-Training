import threading
import time

def task_1():
    print("task-1 started")
    time.sleep(3)
    print("task-1 finished")

def task_2():
    print("task-2 started")
    time.sleep(2)
    print("task-2 finished")

thread1 = threading.Thread(target=task_1)
thread2 = threading.Thread(target=task_2)

thread1.start() # Wt-1
thread2.start() #Wt-2

##############################################

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print("run() method started..", threading.current_thread().name)
        time.sleep(3)
        print("run() method ended..", threading.current_thread().name)

thread1 = MyThread()
thread2 = MyThread()

thread1.start()
thread2.start()