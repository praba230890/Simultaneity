import requests

import time
start_time = time.perf_counter()

data1 = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data2 = requests.get("https://jsonplaceholder.typicode.com/todos/2")
data3 = requests.get("https://jsonplaceholder.typicode.com/todos/3")
data4 = requests.get("https://jsonplaceholder.typicode.com/todos/4")

print(data1.json())
print(data2.json())
print(data3.json())
print(data4.json())
end_time = time.perf_counter()
print(end_time - start_time, "seconds")
