import random
from multiprocessing import Process
from InsertionSortProcess import InsertionSorter
from SelectionSortProcess import SelectionSorter
from MergeSortProcess import MergeSorter
from QuickSortProcess import QuickSorter


class SortingProcesses:

    def __init__(self):
        pass

    def processes(self):
        num_array = SortingProcesses.array_generator(10)
        insertion_sorter = InsertionSorter(num_array)
        selection_sorter = SelectionSorter(num_array)
        merge_sorter = MergeSorter(num_array)
        quick_sorter = QuickSorter(num_array)
        selection_sorter.start()
        insertion_sorter.start()
        merge_sorter.start()
        quick_sorter.start()



    @staticmethod
    def array_generator(size):
        num_array = []
        for index in range(0, size):
            num = random.randint(0, 100)
            while num in num_array:
                num = random.randint(0, 100)
            num_array.append(num)

            #2147483647-1
        return num_array


test = SortingProcesses()
test.processes()

