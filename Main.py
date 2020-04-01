import random
class Main:


    @staticmethod
    def ArrayGenerator(size):
        list = []
        for index in range(0, size):
            list[index] = random.randint(0, 2147483647)
            return index

