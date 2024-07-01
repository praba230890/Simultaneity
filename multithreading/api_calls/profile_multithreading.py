import requests

import threading
import time
start_time = time.perf_counter()

class MyThread(threading.Thread):

    def run(self):
       data1 = self._target(*self._args, **self._kwargs)
       print(data1.json())

x1 = threading.Thread(target=requests.get, args=("https://jsonplaceholder.typicode.com/todos/1",))
x1.start()

x2 = threading.Thread(target=requests.get, args=("https://jsonplaceholder.typicode.com/todos/2",))
x2.start()

x3 = threading.Thread(target=requests.get, args=("https://jsonplaceholder.typicode.com/todos/3",))
x3.start()

x4 = threading.Thread(target=requests.get, args=("https://jsonplaceholder.typicode.com/todos/4",))
x4.start()

x1.join()
x2.join()
x3.join()
x4.join()


end_time = time.perf_counter()
print(end_time - start_time, "seconds")
