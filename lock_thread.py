import threading, queue
import time


lock = threading.Lock()
q = queue.Queue()

c = 0

def task(i):
    global c
    d = 0
    for v in range(100000):
        d += 1
    with lock:
        c += d
    print("Thread %s" % (i))

if __name__ == "__main__":
    tasks = []
    for i in range(100):
        add_task = threading.Thread(target=task, args=(i,))
        add_task.start()
        tasks.append(add_task)
    
    for task in tasks:
        task.join()
    
    print("Final result of 100 times 100000: %s" % c)