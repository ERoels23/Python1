from DistortedInt import DistortedInt
from itertools import combinations, permutations
from functools import reduce

class DistortedIntegers:
    # initialisation
    def __init__(self, n, alpha):
        self.alpha = alpha
        self.n = n
        self.gen = (DistortedInt(x, self.n, self.alpha) for x in range(self.n))

    # def gen(self):
    #     return
    #     for x in range(self.n):
    #         yield DistortedInt(x, self.n, self.alpha)
    #     #
    # overwrite "print"
    def __str__(self):
        # for x in range(self.n):
        #     print(DistortedInt(x, self.n, self.alpha))
        for x in self.gen:
            return str(x)

    def size(self):
        return self.n


# class IteratorOfDistortedIntegers:
#     # d is type DistortedIntegers
#     def __init__(self, d):
#         self.distortedInteger = d
#         self.start = 0
#         self.end = d.size() - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start <= self.end:
#             self.start += 1
#             return DistortedInt(self.start-1, self.distortedInteger.n, self.distortedInteger.alpha)
#         raise StopIteration

class IteratorOfDistortedIntegers:
    # d is type DistortedIntegers
    def __init__(self, d):
        self.distortedInteger = d

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.distortedInteger.gen)



def HasDistortedEquationProperty(n,alpha):
    successes = []
    for x in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
        for z in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
            # for any x and z there is a unique y for x*y = z
            count = 0
            # check every y for x and z
            for y in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
                if (x*y == z):
                    count++
            # add count of equality holding
            successes.append(count)
    # return true if unique, ie. all counts are == 1
    return all(count == 1 for count in successes)



def TestHasDistortedEquationProperty():
    l = []
    for n in range(1,21):
        for alpha in range(n):
            if HasDistortedEquationProperty(n,alpha):
                l.append((n,alpha))
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

# recursive function to continue down branches
def recursiveResultFinder(generators: [DistortedInt], current, results):
    '''
    recursive function to find span of DistortedInt tree
    param generators: list of distorted integers we are checking span of tree with
    param current: our current result from previous multiplications of DistortedInts
    param results: our list of results from multiplications of DistortedInts (stored in String format)
    '''
    for val in generators:
        res = current * val
        # result is in our list of results, cut off branch
        if str(res) in results:
            continue
        # if our current result is not in our list of previous results, continue down branch
        else:
            results.append(str(res))
            # recurse down branch with our result and list of results
            recursiveResultFinder(generators, res, results)

# initialiser to find span of distortedInt tree
def spanInit(generators: [DistortedInt]):
    '''
    initialiser for recursive function to determine span of the DistortedInt tree
    param generators: list of distorted integers we are checking span of tree with
    '''
    # start with empty list of results to pass into our recursive function
    results = []
    for gen in generators:
        # begin recursion
        recursiveResultFinder(generators, gen, results)
    return results # return list of distortedInts in tree span found

if __name__ == '__main__':
    a = DistortedInt(1,5,3)
    b = DistortedInt(2,5,3)
    # c = DistortedInt(6,7,3)

    vals = [a,b]
    # test = calc(vals)
    #
    # for i in test:
    #     print(i)

    s = spanInit(vals)
    s.sort()
    for i in s:
        print(i)

    print("Testing Distorted Equation Property: " + str(TestHasDistortedEquationProperty()))


    for x in IteratorOfDistortedIntegers(DistortedIntegers(3,2)):
        print(x)
