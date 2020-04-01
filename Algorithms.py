class Sorts:
    @staticmethod
    def insertion_sort(params):
        for index in range(1, len(params)):
            num = index
            while num >= 1 and params[num] < params[num-1]:
                Sorts.swap(params, num - 1, num)
                num -= 1
        return params

    @staticmethod
    def selection_sort(params):
        for index in range (1, len(params)):
            minim = float('inf')
            swapper = index
            for num in range(index, len(params)):
                if params[num] < minim:
                    swapper = num
            Sorts.swap(params, swapper, index)
        return params

    @staticmethod
    def quick_sort(params):
        Sorts.quick_sorter(params, 0, len(params) - 1)
        return params



    @staticmethod
    def merge_sort(params):
        Sorts.merge_sorter(params, 0, len(params))
        return params








    @staticmethod
    def quick_sorter(params, start, end):
        if start < end:

            part = Sorts.partition(params, start, end)

            Sorts.quick_sorter(params, start, part - 1)

            Sorts.quick_sorter(params, part + 1, end)

    @staticmethod
    def partition(params, start, end):
        piv = params[end]
        checker = start-1
        for indexer in range(start, end):
            if params[indexer] < piv:
                checker += 1
                Sorts.swap(params, indexer, checker)

        Sorts.swap(params, checker + 1, end)
        return checker+1

    @staticmethod
    def merge_sorter(params, start, end):
        if end - start <= 1:
            return
        mid = int((start + end) / 2)
        Sorts.merge_sorter(params, start, mid)
        Sorts.merge_sorter(params, mid, end)

        Sorts.merge(params, start, mid, end)



    @staticmethod
    def merge(params, start, mid, end):
        final = []
        num_one = start
        num_two = mid
        while num_one != mid or num_two != end:
            if num_one == mid:
                final.append(params[num_two])
                num_two += 1
            elif num_two == end:
                final.append(params[num_one])
                num_one += 1
            elif params[num_one] < params[num_two]:
                final.append(params[num_one])
                num_one += 1
            else:
                final.append(params[num_two])
                num_two += 1
        for index in range(0, len(final)):
            params[index+start] = final[index]

    @staticmethod
    def heap_sort(params):
        return 0

    @staticmethod
    def swap(params, one, two):
        temp = params[one]
        params[one] = params[two]
        params[two] = temp


