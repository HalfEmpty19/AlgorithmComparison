class Algorithms:
    @staticmethod
    def insertion_sort(params):
        for index in range(1, len(params)):
            num = index
            while num >= 1 and params[num] < params[num-1]:
                temp = params[num]
                params[num] = params[num-1]
                params[num-1] = temp
                num -= 1
        return params

    @staticmethod
    def selection_sort(params):
        for index in range (1, len(params)):
            minim = float('inf')
            for num in range(index, len(params)):
                if params[num] < minim:
                    minim = params[num]
                    swapper = num
            params[swapper] = params[index]
            params[index] = minim
        return params

    @staticmethod
    def quick_sort(params):
        return params

    @staticmethod
    def merge_sort(params):
        if len(params) <= 1:
            return params
        mid = len(params)/2
        tempone = Algorithms.merge_sort(params[0:mid])
        temptwo = Algorithms.merge_sort(params[mid:])

        return Algorithms.merge(tempone, temptwo)



        return params
    @staticmethod
    def merge(one, two):
        mid = (len(one) + len(two))/2


    @staticmethod
    def heap_sort(params):
        return 0


list = [0, 3, 2, 5, 8, 1, 8, 5, 81, 21941, 214125,1251 ,2512,5,12]
