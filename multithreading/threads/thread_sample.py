import threading


class MyThread(threading.Thread):

    def run(self):
        print(self)
        print(self._args, self._kwargs)
        self._target(*self._args, **self._kwargs)

mt = MyThread(target=print, args=("hellow world!",))

mt.start()

mt.join()