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


def calc(distortedInts):
    resultSet = set()
    # go through every number of combinations ex. [1,2,3] = permute 2, permute 3
    for i in range(2, len(distortedInts)+1):
        # go through every possible combination
        for k in permutations(distortedInts, i):
            result = reduce((lambda x, y: x * y), k)
            # converted to string to avoid duplicate distorted ints
            resultSet.add(str(result))
    return resultSet

def recursiveResultFinder(generators: [DistortedInt], current, results):
    for val in generators:
        res = current * val
        # result is in our list of results, cut off branch
        if str(res) in results:
            continue
        # if our current result is not in our list of previous results, continue down branch
        else:
            results.add(str(res))
            # recurse down branch with our result and list of results
            recursiveResultFinder(generators, res, results)

# initialiser to find span of distortedInt tree
def spanInit(generators: [DistortedInt]):
    results = set()
    for gen in generators:
        results.add(str(gen))
        # begin recursion
        recursiveResultFinder(generators, gen, results)
    return results # return list of distortedInts in tree span found

if __name__ == '__main__':
    a = DistortedInt(4,7,3)
    b = DistortedInt(5,7,3)
    c = DistortedInt(6,7,3)

    vals = [a,b,c]
    # test = calc(vals)
    #
    # for i in test:
    #     print(i)

    s = spanInit(vals)
    for i in s:
        print(i)

    print("Testing Distorted Equation Property: " + str(TestHasDistortedEquationProperty()))


    # for x in IteratorOfDistortedIntegers(DistortedIntegers(3,2)):
    #     print(x)
