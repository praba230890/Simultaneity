import time
from collections import deque
import heapq


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


class AsyncQueue:
    def __init__(self):
        self.items = deque()
        self.waiting = deque()

    def put(self, item):
        self.items.append(item)
        if self.waiting:
            func = self.waiting.popleft()
            sched.call_soon(func)

    def get(self, callback):
        if self.items:
            callback(self.items.popleft())
        else:
            self.waiting.append(lambda: self.get(callback))

def producer(q, count):
    def _run(n):
        if n < count:
            print("producing: ", n)
            q.put(n)
            sched.call_later(1, lambda: _run(n+1))
    _run(0)

def consumer(q):
    def _consume(item):
        if item is None:
            pass
        else:
            print("consuming item: ", item)
            sched.call_soon(lambda: consumer(q))
    q.get(callback=_consume)

q = AsyncQueue()
sched.call_soon(lambda: producer(q, 10))
sched.call_soon(lambda: consumer(q,))
sched.run()