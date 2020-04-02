from multiprocessing import Process
from Algorithms import Sorts


class InsertionSorter(Process):
    num_sorted = 0
    num_array = []

    def __init__(self, params):
        super(InsertionSorter, self).__init__()
        self.num_array = params

    def run(self):
        self.insertion_sort(self.num_array)


    def insertion_sort(self, params):
        for index in range(1, len(params)):
            num = index
            while num >= 1 and params[num] < params[num - 1]:
                Sorts.swap(params, num - 1, num)
                num -= 1
            self.num_sorted += 1
        return params
