import time
from collections import deque

class Scheduler:
    def __init__(self) -> None:
        self.ready = deque()

    def call_soon(self, func) -> None:
        self.ready.append(func)

    def run(self) -> None:
        while self.ready:
            func = self.ready.popleft()
            func()

sched = Scheduler()

def countdown(n):
    if n > 0:
        print("Down: ", n)
        time.sleep(1)
        sched.call_soon(lambda: countdown(n-1))

def countup(stop, x=0):
    if x < stop:
        print("Up: ", x)
        time.sleep(1)
        sched.call_soon(lambda: countup(stop, x+1))

sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(5))

sched.run()