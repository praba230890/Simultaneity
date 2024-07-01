import threading
import queue
import time 

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    q.join()
    q.put(item)
    time.sleep(1)

# Block until all tasks are done.
# q.join()
print('All work completed')