import unittest
from DistortedInt import *
from DistortedIntegers import *

class TestingDistortedInt(unittest.TestCase):
    # Idempotent Property
    def test_HasDistortedIdempotentProperty(self):
        print("\nTesting Idempotent Property: ")
        flipper = True
        for n in range(1, 101):
            for alpha in range(n):
                if (not HasDistortedIdempotentProperty(n, alpha)):
                    flipper = False
        self.assertTrue(flipper)
    # Distorted Roots of One
    def test_DistortedRootsOfOne(self):
        print("\nTesting Roots of One: ")
        flipper = True
        for n in range(2,101):
            for alpha in range(n):
                if (len(DistortedRootsOfOne(n, alpha)) != 1):
                    flipper = False
        self.assertTrue(flipper)
    # Commutative Distorted Multiplication
    def test_CommutativeDistortedMultiplication(self):
        l = []
        for n in range(1, 101):
            for alpha in range(n):
                if IsCommutativeDistortedMultiplication(n, alpha):
                    l.append((n,alpha))
        print("\nTesting Commutative Multiplication: " + str(l))
        print("\nTesting all odd modulus Commutative Multiplication: " + str(all(n % 2 != 0 for (n,a) in l)))
        flipper = True
        for n in range(1, 101):
            for alpha in range(n):
                if (IsCommutativeDistortedMultiplication(n, alpha) and n % 2 == 0):
                    print("n: " + str(n) + "  " + "a: " + str(alpha))
                    flipper = False
        self.assertTrue(flipper)

    # Associative Distorted Multiplication
    # produces the list of (n,a) pairs
    # check through the list
    def test_AssociativeDistortedMultiplication(self):
        print("\nTesting Associative Distorted Multiplication: ")
        assoc = []
        for n in range(1,21):
            for a in range(n):
                if IsAssociativeDistortedMultiplication(n, a):
                    assoc.append((n,a))
        print(str(assoc))
        flipper = True
        for (n,a) in assoc:
            for x in range(n):
                first = DistortedInt(x,n,a)
                for y in range(x,n):
                    second = DistortedInt(y,n,a)
                    for z in range(y,n):
                        third = DistortedInt(z,n,a)
                        if (((first*second)*third) != (first*(second*third))):
                            flipper = False
        self.assertTrue(flipper)
    # Quasi Distributive Distorted Multiplication
    # NOTE: only produces (n,alpha) pairs, doesn't check beyond that
    def test_QuasiDistributiveDistortedMultiplication(self):
        print("\nTesting Quasi Distributive Multiplication: ")
        l = []
        for n in range(1, 21):
            for alpha in range(n):
                if (IsQuasiDistributiveDistortedMultiplication(n, alpha)):
                    l.append((n, alpha))
        print(str(l))

if __name__ == '__main__':
    unittest.main()
    # lines to run at end of test
