import threading
import time

def process_data():
    time.sleep(3)

thread = threading.Thread(target=process_data)

thread.start()
print(thread.is_alive())

thread.join()

print(thread.is_alive())