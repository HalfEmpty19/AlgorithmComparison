from multiprocessing import Process
from Algorithms import Sorts

class QuickSorter(Process):
    num_sorted = 0
    num_array = []

    def __init__(self, params):
        super(QuickSorter, self).__init__()
        self.num_array = params

    def run(self):
        self.quick_sort(self.num_array)

    def quick_sort(self, params):
        self.quick_sorter(params, 0, len(params) - 1)

    def quick_sorter(self, params, start, end):
        if start < end:
            part = self.partition(params, start, end)

            self.quick_sorter(params, start, part - 1)

            self.quick_sorter(params, part + 1, end)

    def partition(self, params, start, end):
        self.num_sorted+=1
        print(self.num_sorted)
        piv = params[end]
        checker = start - 1
        for indexer in range(start, end):
            if params[indexer] < piv:
                checker += 1
                Sorts.swap(params, indexer, checker)

        Sorts.swap(params, checker + 1, end)
        return checker + 1