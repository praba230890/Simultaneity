# Threads:

## Two ways to create/start threads.
 - From functions
 - By subclassing Thread class and create a new Thread class

### From functions:

```python
import threading
import time

def task(a, b):
    time.sleep(1)
    print("The result of addition is: %s" % (a + b))

if __name__ == "__main__":
    add_task = threading.Thread(target=task, args=(5,5,))
    add_task.start()
    add_task.join()
```
### When to use:
 - when you want to call the function on either child threads or the main thread (used at many place in your app)
 - when you already have an independent function used elsewhere and need to scale it parallely
 - easy to understand and during prototype development

### By Subclassing Thread class

```python
import time
import threading

class AddThread(threading.Thread):

    def __init__(self, a, b, name=None):
        super().__init__(name=name)
        self.a = a
        self.b = b

    def run(self):
        time.sleep(1)
        print("The result of addition is: %s" % (self.a + self.b))

if __name__ == "__main__":
    t = AddThread(5, 5)
    t.start()
    t.join()
```

### When to use:
 - If the code to be executed inside the thread is not used anywhere else 
 - If the application code is written/maintained in a more object oriented way
 - Code will be clean and organized


threads in python and other languages (bonus os threads)
is race condition possible?
how to avoid race condition (different ways - lock, semaphore, etc)
where to put the lock (only during update and try to minimize the updates as less as possible)

Don't to this
```python
import threading
import time


lock = threading.Lock()

c = 0

def task(a, b, i):
    global c
    for v in range(100000):
        with lock:
            c += 1
    print("The result of addition is: %s for thread %s" % (a + b, i))


if __name__ == "__main__":
    tasks = []
    for i in range(100):
        add_task = threading.Thread(target=task, args=(5,5,i,))
        add_task.start()
        tasks.append(add_task)
    
    time.sleep(2)

print(c)
```

do this
```python
import threading
import time


lock = threading.Lock()

c = 0

def task(a, b, i):
    global c
    d = 0
    for v in range(100000):
        d += 1
    print("The result of addition is: %s for thread %s" % (a + b, i))
    with lock:
        c += d

if __name__ == "__main__":
    tasks = []
    for i in range(100):
        add_task = threading.Thread(target=task, args=(5,5,i,))
        add_task.start()
        tasks.append(add_task)
    
    time.sleep(2)

print(c)
```

exception handling in thread
exception handling around the thread and inside the thread
dead lock
moving away from lock
thread limits (min(32, os.cpu_count+4))