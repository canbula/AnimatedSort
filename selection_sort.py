import random
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib


class SelectionSort:
    def __init__(self, unsorted_list, limit):
        self.ul = unsorted_list
        self.ol = self.ul
        self.d = 0
        self.limit = limit
        self.done = False
        self.t1 = 0
        self.t2 = 0
        matplotlib.use("TkAgg")
        plt.rcParams["figure.figsize"] = [8, 6]
        self.fig, self.ax = plt.subplots()

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1

    def ul_to_ol(self):
        m = self.limit
        s = 0
        for i in range(self.d, len(self.ol)):
            if self.ol[i] < m:
                m = self.ol[i]
                s = i
        self.ol[self.d], self.ol[s] = self.ol[s], self.ol[self.d]
        self.d += 1
        if self.d == len(self.ol):
            self.done = True

    def ax_properties(self):
        self.ax.clear()
        self.ax.set_ylim([0, self.limit])
        self.ax.set_title("Animated Sort")

    def init(self):
        self.tic()
        self.ax_properties()
        self.ax.bar([i for i in range(len(self.ul))], self.ul)

    def update(self, _):
        self.ul_to_ol()
        self.ax_properties()
        self.ax.set_title("Sorting {:d} of {:d} elements in {:.2f} seconds".format(self.d + 1,
                                                                                   len(self.ol),
                                                                                   self.toc()))
        self.ax.bar([i for i in range(len(self.ol))], self.ol)
        if self.done:
            time.sleep(3)
            quit()

    def draw(self):
        _ = FuncAnimation(self.fig, self.update, init_func=self.init, save_count=10)
        plt.show()


def main():
    n = 50
    m = 1000
    unsorted_list = random.sample(range(0, m), n)
    selection_sort = SelectionSort(unsorted_list, m)
    selection_sort.draw()
    '''selection_sort.ul_to_ol()'''


if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print("{:e}".format(t2 - t1))
