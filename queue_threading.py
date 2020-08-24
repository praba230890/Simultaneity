import threading, queue
import time

q = queue.Queue(maxsize=1)
q.put(0)

def task(a, b, i):
    d = q.get()
    for v in range(100000):
        d += 1
    print("The result of addition is: %s for thread %s" % (a + b, i))
    q.put(d)
    time.sleep(1)

if __name__ == "__main__":
    tasks = []
    for i in range(100):
        add_task = threading.Thread(target=task, args=(5,5,i,))
        add_task.start()
        tasks.append(add_task)
    for task in tasks:
        task.join()

print(q.get())
q.task_done()