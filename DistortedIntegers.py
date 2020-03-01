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
    for x in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
        for y in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
            # looking for unique y
            if y == x:
                continue
            for z in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
                # looking for unique y
                if y == z:
                    continue
                if (x*y == z):
                    print()
                    print(x)
                    print(z)
                    print(y)
                    print()
                    return True
    return False


def TestHasDistortedEquationProperty():
    l = []
    for n in range(1,21):
        for alpha in range(n):
            if HasDistortedEquationProperty(n,alpha):
                l.append("n: " + str(n) + " " + "alpha: " + str(alpha))
    return l


def calc(distortedInts):
    resultSet = set()
    useCombos = False
    # if associative, ie. odd modulus, so x*y = y*x
    if distortedInts[0].n % 2 != 0:
        useCombos = True
    for i in range(2, len(distortedInts)+1):
        if(len(resultSet) == 2):
            print("")
        # if associative, ie. odd modulus, so x*y = y*x
        if (useCombos):
            for j in combinations(distortedInts, i):
                result = reduce((lambda x, y: x * y), j)
                resultSet.add(str(result))
        else:
            for k in permutations(distortedInts, i):
                result = reduce((lambda x, y: x * y), k)
                resultSet.add(str(result))
    return resultSet



if __name__ == "__main__":
    a = DistortedInt(1,5,3)
    b = DistortedInt(4,5,3)
    c = DistortedInt(3,5,3)
    d = DistortedInt(2,5,3)
    e = DistortedInt(0,5,3)
    test = [a,b,c,d,e]
    r = calc(test)

    for i in r:
        print(i)

    print("Testing Distorted Equation Property: " + str(TestHasDistortedEquationProperty()))


    # for x in IteratorOfDistortedIntegers(DistortedIntegers(3,2)):
    #     print(x)
