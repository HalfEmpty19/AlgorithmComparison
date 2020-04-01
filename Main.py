import random
from multiprocessing import Process

from Algorithms import Sorts


class SortingProcesses:

    def __init__(self):
        pass

    def processes(self):
        num_array = SortingProcesses.array_generator()
        insertion_sorter = Process(target=Sorts.insertion_sort, args=(num_array,))
        selection_sorter = Process(target=Sorts.selection_sort, args=(num_array,))
        merge_sorter = Process(target=Sorts.merge_sort, args=(num_array,))
        quick_sorter = Process(target=Sorts.quick_sort, args=(num_array,))
        insertion_sorter.start()
        selection_sorter.start()
        merge_sorter.start()
        quick_sorter.start()


    @staticmethod
    def array_generator(size):
        num_array = []
        for index in range(0, size):
            num_array.append(random.randint(0, 2147483647-1))
        return num_array


test = SortingProcesses()
test.processes()

