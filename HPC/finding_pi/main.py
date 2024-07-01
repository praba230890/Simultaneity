from threading import Thread
import os

from bc import FindPi
from timer import TicToc

USE_THREADS = True

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()

    

    n = 100000000

    if USE_THREADS:
        start = end = 0
        find_threads = []
        methods = []
        for i in range(os.cpu_count()):
            points_per_thread = n//os.cpu_count()
            finding_pi = FindPi()
            find_thread = Thread(target=finding_pi.throw_points, args=(start, start+points_per_thread,))
            print(f"starting thread with start: {start} & end: {start+points_per_thread}")
            find_thread.start()
            find_threads.append(find_thread)
            methods.append(finding_pi)

            start += points_per_thread
        
        ii = []
        nn = []
        for i, find_thread in enumerate(find_threads):
            find_thread.join()
            finding_pi = methods[i]
            ii.append(finding_pi.i)
            nn.append(finding_pi.n)
            print(f"PI = {finding_pi.value_of_pi} | N = {finding_pi.i}/{finding_pi.n} | TIME = {tt.toc()}")


        print(f"PI = {FindPi.aggregate_pi(ii, nn)} | TIME = {tt.toc()}")

    else:
        finding_pi = FindPi()
        finding_pi.throw_points(0, n)
        # find_thread = Thread(target=finding_pi.throw_points, args=(n,))
        # find_thread.start()

        # find_thread.join()

        print(f"PI = {finding_pi.value_of_pi} | N = {finding_pi.i}/{finding_pi.n} | TIME = {tt.toc()}")