import unittest
from DistortedInt import *
from DistortedIntegers import *

class TestingDistortedInt(unittest.TestCase):
    def test_HasDistortedIdempotentProperty(self):
        self.assertTrue(TestHasDistortedIdempotentProperty())
    def test_DistortedRootsOfOne(self):
        self.assertTrue(TestDistortedRootsOfOne())
    def test_CommutativeDistortedMultiplication(self):
        self.assertTrue(TestIsCommutativeDistortedMultiplication())
    def test_AssociativeDistortedMultiplication(self):
        flipper = True
        for (n,a) in TestIsAssociativeDistortedMultiplication():
            for x in range(n):
                first = DistortedInt(x,n,a)
                for y in range(x,n):
                    second = DistortedInt(y,n,a)
                    for z in range(y,n):
                        third = DistortedInt(z,n,a)
                        if (((first*second)*third) != (first*(second*third))):
                            flipper = False
        self.assertTrue(flipper)



if __name__ == '__main__':
    unittest.main()
