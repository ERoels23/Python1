from DistortedInt import DistortedInt
from itertools import combinations, permutations
from functools import reduce

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

def HasDistortedEquationProperty(n,alpha):
    l = []
    for x in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
        for y in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
            for z in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
                if (x*y == z):
                    l.append(y)
    # unique y, so much be length 1
    return len(l) == 1


def TestHasDistortedEquationProperty():
    l = []
    for n in range(1,21):
        for alpha in range(n):
            if HasDistortedEquationProperty(n,alpha):
                l.append("n: " + str(n) + " " + "alpha: " + str(alpha))
    return l


# def calc(distortedInts):
#     resultSet = set()
#     # go through every number of combinations ex. [1,2,3] = permute 2, permute 3
#     for i in range(2, len(distortedInts)+1):
#         # go through every possible combination
#         for k in permutations(distortedInts, i):
#             result = reduce((lambda x, y: x * y), k)
#             # converted to string to avoid duplicate distorted ints
#             resultSet.add(str(result))
#     return resultSet

def generatorSpanCalculation(generators: [DistortedInt], current, results):
    for val in generators:
        result = current * val
        # if our current result is not in our list of previous results, continue down branch
        if not (str(result) in results):
            # add to our results, as string
            results.append(str(result))
            # recurse down branch with our result and list of results
            generatorSpanCalculation(generators, result, results)
        # result is in our list of results, cut off branch
        else:
            continue

def spanInit(generators: [DistortedInt]):
    results = []
    for gen in generators:
        # equivalent to gen*gen
        results.append(str(gen))
        # begin recursion
        generatorSpanCalculation(generators, gen, results)
    return results

if __name__ == '__main__':
    x1 = DistortedInt(18,20,11)
    x2 = DistortedInt(7,20,11)
    x3 = DistortedInt(10,20,11)

    vals = [x1,x2,x3]

    print(spanInit(vals))

    print("Testing Distorted Equation Property: " + str(TestHasDistortedEquationProperty()))


    # for x in IteratorOfDistortedIntegers(DistortedIntegers(3,2)):
    #     print(x)
