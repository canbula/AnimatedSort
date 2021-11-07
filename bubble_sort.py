import random
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib


class BubbleSort:
    def __init__(self, unsorted_list, limit):
        self.ul = unsorted_list
        self.ol = self.ul
        self.limit = limit
        self.done = False
        self.t1 = 0
        self.t2 = 0
        self.d = 0
        matplotlib.use("TkAgg")
        plt.rcParams["figure.figsize"] = [8, 6]
        self.fig, self.ax = plt.subplots()

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1

    def ul_to_ol(self):
        for i in range(len(self.ol)):
            self.d = i
            nothing_to_sort = True
            for j in range(len(self.ol)-1):
                input()
                if self.ol[j] > self.ol[j+1]:
                    self.ol[j], self.ol[j+1] = self.ol[j+1], self.ol[j]
                    nothing_to_sort = False
            if nothing_to_sort:
                self.done = True
                break

    def ul_to_ol_1by1(self):
        print(self.d)
        if self.d == len(self.ol)-1:
            self.d = 0
        else:
            if self.ol[self.d] > self.ol[self.d+1]:
                self.ol[self.d], self.ol[self.d+1] = self.ol[self.d+1], self.ol[self.d]
            self.d += 1

    def ul_to_ol_1(self):
        if self.d == len(self.ol):
            self.done = True
        else:
            n = len(self.ol)-self.d
            for i in range(n-1):
                if self.ol[i] > self.ol[i+1]:
                    self.ol[i], self.ol[i+1] = self.ol[i+1], self.ol[i]
            self.d += 1

    def ax_properties(self):
        self.ax.clear()
        self.ax.set_ylim([0, self.limit])
        self.ax.set_title("Animated Sort: Bubble Sort")

    def init(self):
        self.tic()
        self.ax_properties()
        self.ax.bar([i for i in range(len(self.ul))], self.ul)

    def update(self, _):
        self.ul_to_ol_1()
        self.ax_properties()
        self.ax.set_title("Sorting {:d} of {:d} elements in {:.2f} seconds".format(self.d+1,
                                                                                   len(self.ol),
                                                                                   self.toc()))
        self.ax.bar([i for i in range(len(self.ol))], self.ol)
        if self.done:
            time.sleep(3)
            quit()

    def draw(self):
        _ = FuncAnimation(self.fig, self.update, init_func=self.init, interval=10)
        plt.show()


def main():
    n = 500
    m = 10000
    unsorted_list = random.sample(range(0, m), n)
    bubble_sort = BubbleSort(unsorted_list, m)
    bubble_sort.draw()
    '''bubble_sort.ul_to_ol()'''


if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print("{:e}".format(t2 - t1))
