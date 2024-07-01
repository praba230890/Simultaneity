from random import random
import time

start_time = time.perf_counter()

def get_random_numbers(upto=500):
    return [random() for i in range(upto)]

# print(get_random_numbers(5000))
get_random_numbers(50000000)
end_time = time.perf_counter()
print(end_time - start_time, "seconds")
