import unittest
from DistortedInt import *
from DistortedIntegers import *

class TestingDistortedInt(unittest.TestCase):
<<<<<<< Updated upstream
=======

    '''
    DistortedInt Creation
    '''

    # DistortedInt Instantiation Non-null
    def test_NonNullDistortedInt(self):
        print("Testing DistortedInt Creation")
        x = DistortedInt(2, 5, 3)
        self.assertIsInstance(x, DistortedInt)

    # DistortedInt Holds Correct Values
    def test_CorrectArgumentsStored(self):
        x = DistortedInt(2, 5, 3)
        self.assertTrue(x.object == 2 and x.n == 5 and x.alpha == 3)

    # Edge Case 1: alpha = 0, n = 1 (Valid)
    def test_ValidAlphaEdgeCase(self):
        x = DistortedInt(0, 1, 0)
        self.assertIsInstance(x, DistortedInt)

    # Edge Case 2: alpha = 1, n = 1 (Invalid)
    # Note that DistortedInt catches the bubbled exception, doesn't throw it - so we must use ValidateArguments method
    def test_InvalidAlphaEdgeCase(self):
        self.assertRaises(InvalidArgumentException, ValidateArguments, 0, 1, 1)

    # Invalid Case with Negatives
    def test_invalidCaseNegatives(self):
        self.assertRaises(InvalidArgumentException, ValidateArguments, -10, 10, -3)

    # Invalid Case with String args
    def test_invalidCaseStrings(self):
        self.assertRaises(InvalidArgumentException, ValidateArguments, "4", 10, "Hello")


    '''
    DistortedInt Multiplication
    '''

    # Multiplication using values from specification
    def test_ValidOperandsFromSpec(self):
        x = DistortedInt(2, 5, 3)
        y = DistortedInt(4, 5, 3)
        self.assertEqual((x * y), DistortedInt(3, 5, 3))

    # Multiplication using other valid values
    def test_GeneralValidOperands(self):
        x = DistortedInt(7, 15, 9)
        y = DistortedInt(13, 15, 9)
        self.assertEqual((x * y), DistortedInt(4, 15, 9))

    # Invalid Operands throws Exception
    def test_InvalidOperandExceptionThrown(self):
        x = DistortedInt(3, 10, 5)
        y = DistortedInt(13, 17, 6)
        self.assertRaises(InvalidOperandException, print, x * y)

    # Idempotent Property
>>>>>>> Stashed changes
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
