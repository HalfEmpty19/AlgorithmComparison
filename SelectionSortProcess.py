from multiprocessing import Process
from Algorithms import Sorts


class SelectionSorter(Process):
    num_sorted = 0
    num_array = []

    def __init__(self, params):
        super(SelectionSorter, self).__init__()
        self.num_array = params

    def run(self):
        self.selection_sort(self.num_array)


    def selection_sort(self, params):
        for index in range(1, len(params)):
            minim = float('inf')
            swapper = index
            for num in range(index, len(params)):
                if params[num] < minim:
                    swapper = num
            Sorts.swap(params, swapper, index)
            self.num_sorted += 1
        return params
