import threading, queue
import time


q = queue.Queue()

def task(i):
    d = 0
    for v in range(100000):
        d += 1
    q.put(d)
    print("Thread: %s" % (i))
    time.sleep(1)

if __name__ == "__main__":
    tasks = []
    for i in range(100):
        add_task = threading.Thread(target=task, args=(i,))
        add_task.start()
        tasks.append(add_task)
    
    for task in tasks:
        task.join()
    
    out = 0
    while not q.empty():
        out += q.get()
        q.task_done()
    print("Final result of 100 times 100000: %s" % out)