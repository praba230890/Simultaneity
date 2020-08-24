import threading, queue
import time


lock = threading.Lock()
q = queue.Queue()

def task(a, b, i):
    d = 0
    for v in range(100000):
        d += 1
    q.put(d)
    print("The result of addition is: %s for thread %s" % (a + b, i))
    time.sleep(1)

if __name__ == "__main__":
    tasks = []
    for i in range(100):
        add_task = threading.Thread(target=task, args=(5,5,i,))
        add_task.start()
        tasks.append(add_task)
    
    for task in tasks:
        task.join()
    
    out = 0
    while not q.empty():
        out += q.get()
    print(out)