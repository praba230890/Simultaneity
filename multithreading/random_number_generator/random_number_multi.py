import threading
from random import random
import time

start_time = time.perf_counter()

def get_random_numbers(upto=500):
    x = [random() for i in range(upto)]

threads = [threading.Thread(target=get_random_numbers, args=(12500000,)) for i in range(4)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# print(get_random_numbers(5000))
# get_random_numbers(50000000)
end_time = time.perf_counter()
print(end_time - start_time, "seconds")
