from DistortedInt import DistortedInt
from itertools import combinations, permutations
from functools import reduce

class DistortedIntegers:
    # initialisation
    def __init__(self, n, alpha):
        '''
        Construct a new 'DistortedIntegers' object
        Represents the set Z_n for given (n, alpha)

        :param n: the modulus of the DistortedIntegers
        :param alpha: the distortion of the DistortedIntegers
        '''
        self.alpha = alpha
        self.n = n

    def __str__(self):
        '''
        returns a String representation of the DistortedIntegers object
        '''
        return ("Distorted Integers | n = " + str(self.n) + ", alpha = " + str(self.alpha) + " |")

    def size(self):
        '''
        returns the size of the DistortedIntegers object
        (the number of elements in the list of DistortedInt's)
        '''
        return self.n

class IteratorOfDistortedIntegers:
    # d is type DistortedIntegers
    def __init__(self, d):
        '''
        Construct a new IteratorOfDistortedIntegers object

        :param d: the DistortedInteger to iterate through
        '''
        self.distortedInteger = d
        self.start = 0

    def __iter__(self):
        '''
        returns the Iterator object itself
        '''
        return self

    def __next__(self):
        '''
        advances the Iterator to the next element in the list DistortedIntegers
        '''
        if self.start < self.distortedInteger.size():
            self.start += 1
            return DistortedInt(self.start-1, self.distortedInteger.n, self.distortedInteger.alpha)
        else:
            raise StopIteration

def HasDistortedEquationProperty(n,alpha):
    '''
    returns Boolean representing whether x*y = z for given (n, alpha) and unique y
    if so, the Distorted Equation Property holds true for all x,z in Z_n

    :param n: the modulus of the DistortedInt
    :param alpha: the distortion of the DistortedInt
    '''
    successes = []
    for x in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
        for z in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
            # for any x and z there is a unique y for x*y = z
            count = 0
            # check every y for x and z
            for y in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
                if (x*y == z):
                    # add to list of it working
                    count += 1
            # add length of list of equality holding
            successes.append(count)
    # return true if unique, ie. all counts are == 1
    return all(count == 1 for count in successes)

# recursive function to continue down branches
def recursiveResultFinder(generators: [DistortedInt], current, results):
    '''
    recursive function to find span of DistortedInt tree

    :param generators: list of distorted integers we are checking span of tree with
    :param current: our current result from previous multiplications of DistortedInts
    :param results: our list of results from multiplications of DistortedInts (stored in String format)
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

    :param generators: list of distorted integers we are checking span of tree with
    '''
    # start with empty list of results to pass into our recursive function
    results = []
    for gen in generators:
        # begin recursion
        recursiveResultFinder(generators, gen, results)
    return results # return list of distortedInts in tree span found

if __name__ == '__main__':
    # testing purposes only
    vals = [DistortedInt(1,5,3), DistortedInt(2,5,3)]
    print(vals)
    s = spanInit(vals)
    print(s)

#
#
# class DistortedIntegers:
#     # initialisation
#     def __init__(self, n, alpha):
#         '''
#         Construct a new 'DistortedIntegers' object
#         Represents the set Z_n for given (n, alpha)
#
#         :param n: the modulus of the DistortedIntegers
#         :param alpha: the distortion of the DistortedIntegers
#         '''
#         self.alpha = alpha
#         self.n = n
#         self.gen = (DistortedInt(x, self.n, self.alpha) for x in range(self.n))
#
#     def __str__(self):
#         '''
#         returns a String representation of the DistortedIntegers object
#         '''
#         # for x in range(self.n):
#         #     print(DistortedInt(x, self.n, self.alpha))
#         for x in self.gen:
#             return str(x)
#
#     def size(self):
#         '''
#         returns the size of the DistortedIntegers object
#         (the number of elements in the list of DistortedInt's)
#         '''
#         return self.n
#
# class IteratorOfDistortedIntegers:
#     # d is type DistortedIntegers
#     def __init__(self, d):
#         '''
#         Construct a new IteratorOfDistortedIntegers object
#
#         :param d: the DistortedIntegers list to be iterated through
#         '''
#         self.distortedInteger = d
#
#     def __iter__(self):
#         '''
#         returns the Iterator object itself
#         '''
#         return self
#
#     def __next__(self):
#         '''
#         advances the Iterator to the next element in the list DistortedIntegers
#         '''
#         return next(self.distortedInteger.gen)
