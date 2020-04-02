from multiprocessing import Process


class MergeSorter(Process):
    num_sorted = 0
    num_array = []

    def __init__(self, params):
        super(MergeSorter, self).__init__()
        self.num_array = params

    def run(self):
        self.merge_sort(self.num_array)


    def merge_sort(self, params):
        self.merge_sorter(params, 0, len(params))
        return params



    def merge_sorter(self, params, start, end):
        if end - start <= 1:
            return
        mid = int((start + end) / 2)

        self.merge_sorter(params, start, mid)
        self.merge_sorter(params, mid, end)

        self.merge(params, start, mid, end)



    def merge(self, params, start, mid, end):
        self.num_sorted+=1
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


