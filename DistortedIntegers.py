from DistortedInt import DistortedInt
from itertools import combinations
import numpy

class DistortedIntegers:
    # initialisation
    def __init__(self, n, alpha):
        self.alpha = alpha
        self.n = n

    # def gen(self):
    #     return (DistortedInt(x, self.n, self.alpha) for x in range(self.n))
    #     for x in range(self.n):
    #         yield DistortedInt(x, self.n, self.alpha)
    #     #
    # overwrite "print"
    # def __str__(self):
    #     for x in self.gen(self):
    #         print(x)

    def size(self):
        return self.n - 1


class IteratorOfDistortedIntegers:
    # d is type DistortedIntegers
    def __init__(self, d):
        self.distortedInteger = d
        self.start = 0
        self.end = d.size()

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            self.start += 1
            return DistortedInt(self.start-1, self.distortedInteger.n, self.distortedInteger.alpha)
        raise StopIteration




if __name__ == "__main__":
    test = [1,2,3,4]
    list = []
    for i in range(1, len(test)):
        result = 1
        for j in combinations(test, i):
            for k in j:
                result *= k
        list.append(result)

    for y in list:
        print(y)

    for x in IteratorOfDistortedIntegers(DistortedIntegers(3,2)):
        print(x)
