import threading, queue
import time


lock = threading.Lock()
q = queue.Queue()

c = 0

def task(a, b, i):
    global c
    d = 0
    for v in range(100000):
        d += 1
    with lock:
        c += d
    print("The result of addition is: %s for thread %s" % (a + b, i))

if __name__ == "__main__":
    tasks = []
    for i in range(100):
        add_task = threading.Thread(target=task, args=(5,5,i,))
        add_task.start()
        tasks.append(add_task)
    
    for task in tasks:
        task.join()

print(c)