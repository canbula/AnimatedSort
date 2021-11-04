import random
import time
from threading import Thread
import os
from numba import jit
from numba.typed import List


class SingleSelectionSort:
    def __init__(self, d, ul):
        self.d = d
        self.ul = ul
        self.s = 0

    @staticmethod
    @jit(nopython=True, nogil=True)
    def find_position_static(d, ul):
        s = 0
        for i in range(0, len(ul)):
            if ul[d] > ul[i]:
                s += 1
        return s

    def find_position(self):
        self.s = self.find_position_static(self.d, self.ul)


def main():
    n = 5000
    m = 1000000
    ul = random.sample(range(0, m), n)
    typed_ul = List()
    [typed_ul.append(x) for x in ul]
    done = False
    d = 0
    t = 0
    s = []
    while not done:
        threads = []
        single_selection_sorts = []
        t = min(len(ul), t + os.cpu_count())
        j = 0
        for i in range(d, t):
            single_selection_sorts.append(SingleSelectionSort(i, typed_ul))
            threads.append(Thread(target=single_selection_sorts[j].find_position))
            j += 1
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        for single_selection_sort in single_selection_sorts:
            s.append(single_selection_sort.s)
        if t >= len(ul):
            done = True
        else:
            d = t
    ol = [0 for _ in range(len(ul))]
    for i in range(len(ul)):
        ol[s[i]] = ul[i]


if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print("{:e}".format(t2 - t1))
