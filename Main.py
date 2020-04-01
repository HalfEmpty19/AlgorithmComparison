import random
from multiprocessing import Process

from Algorithms import Sorts


class SortingProcesses:

    def __init__(self):
        pass

    def processes(self):
        list = SortingProcesses.ArrayGenerator(5000)
        insertion_sorter = Process(target=Sorts.insertion_sort, args=(list,))
        selection_sorter = Process(target=Sorts.selection_sort, args=(list,))
        insertion_sorter.start()
        selection_sorter.start()

    @staticmethod
    def ArrayGenerator(size):
        list = []
        for index in range(0, size):
            list.append(random.randint(0, 2147483647-1))
        return list


test = SortingProcesses()
test.processes()

