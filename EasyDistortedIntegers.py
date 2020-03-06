from DistortedIntegers import DistortedIntegers
from DistortedIntegers import IteratorOfDistortedIntegers
from DistortedInt import DistortedInt

# needs to be tested more, but works as far as I can tell
def IterDistortedIdempotentProperty(n,a):
    # range of Zn (ex. Z1 = {0} as provided in spec)
    for i in IteratorOfDistortedIntegers(DistortedIntegers(n,a)):
        if i*i != i:
            return False
    return True

# returns the empty list for n=1, a=0, this should not happen, come back to
def IterDistortedRootsOfOne(n,a):
    lst = []
    for i in IteratorOfDistortedIntegers(DistortedIntegers(n,a)):
        if i*i == DistortedInt(1,n,a):
            lst.append(i*i)
    return lst

def IterIsCommutativeDistortedMultiplication(n, alpha):
    for x in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
        for y in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
            # avoids redundant checks, way of saying range(x, n)
            if y.object < x.object:
                continue
            if (x*y != y*x):
                return False
    return True

def IterIsAssociativeDistortedMultiplication(n, alpha):
    for x in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
        for y in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
            for z in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
                if (((x*y)*z) != (x*(y*z))):
                    return False
    return True


def IterIsQuasiDistributiveDistortedMultiplication(n, alpha):
    for x in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
        for y in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
            for z in IteratorOfDistortedIntegers(DistortedIntegers(n,alpha)):
                if (((x*y)*z) != ((x*y)*(x*z))):
                    return False
    return True

# main for testing purposes...
if __name__ == "__main__":
    print("Testing Idempotent Property: " + str(TestHasDistortedIdempotentProperty()))
    print("Testing Roots of One: " + str(TestDistortedRootsOfOne()))
    commutativeList = TestIsCommutativeDistortedMultiplication()
    print("Testing Commutative Multiplication: " + str(commutativeList))
    print("Testing all odd modulus Commutative Multiplication: " + str(all(n % 2 != 0 for (n,a) in commutativeList)))
    print("Testing Quasi Distributive Multiplication: " + str(TestIsQuasiDistributiveDistortedMultiplication()))
    print("Testing Associative Distorted Multiplication: " + str(TestIsAssociativeDistortedMultiplication()))
