import unittest
import coverage
from DistortedInt import *
from DistortedIntegers import *
from EasyDistortedIntegers import *

class TestingDistortedInt(unittest.TestCase):
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
        self.assertRaises(InvalidOperandException, ValidateOperands, x, y)


    '''
    Additional Requirements
    '''
    
    # Idempotent Property
    def test_HasDistortedIdempotentProperty(self):
        print("\nTesting Idempotent Property: ")
        flipper = True
        for n in range(1, 101):
            for alpha in range(n):
                if (not HasDistortedIdempotentProperty(n, alpha)):
                    flipper = False
        self.assertTrue(flipper)
        print("\nTesting Idempotent Property (with Iterator): ")
        for n in range(1, 101):
            for alpha in range(n):
                if (not IterDistortedIdempotentProperty(n, alpha)):
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
        print("\nTesting Roots of One (with Iterator): ")
        for n in range(2,101):
            for alpha in range(n):
                if (len(IterDistortedRootsOfOne(n, alpha)) != 1):
                    print(n)
                    print(alpha)
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
        print("\nTesting for All Odd Modulus: " + str(all(n % 2 != 0 for (n,a) in l)))
        flipper = True
        for n in range(1, 101):
            for alpha in range(n):
                if (IsCommutativeDistortedMultiplication(n, alpha) and n % 2 == 0):
                    print("n: " + str(n) + "  " + "a: " + str(alpha))
                    flipper = False
        self.assertTrue(flipper)
        print("\nTesting Commutative Mult with Iterator: ")
        q = []
        for n in range(1, 101):
            for alpha in range(n):
                if IterIsCommutativeDistortedMultiplication(n, alpha):
                    q.append((n,alpha))
        self.assertTrue(l == q)

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
        print("\nTesting Associative Distorted Mult with Iterator: ")
        assoc2 = []
        for n in range(1,21):
            for a in range(n):
                if IterIsAssociativeDistortedMultiplication(n, a):
                    assoc2.append((n,a))
        self.assertTrue(assoc == assoc2)
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
        print("\nTesting Quasi Distributive Mult with Iterator: ")
        q = []
        for n in range(1, 21):
            for alpha in range(n):
                if (IterIsQuasiDistributiveDistortedMultiplication(n, alpha)):
                    q.append((n,alpha))
        self.assertTrue(q == l)
    # Distorted Equation Property
    def test_DistortedEquationProperty(self):
        print("Testing Distorted Equation Property: ")
        l = []
        for n in range(1,21):
            for alpha in range(n):
                if HasDistortedEquationProperty(n,alpha):
                    l.append((n,alpha))
        print(str(l))
    # Distorted Integers (Iterator)
    def test_DistortedIntegers(self):
        print("Testing Distorted Integers Iterator: ")
        l = []
        for x in IteratorOfDistortedIntegers(DistortedIntegers(3,2)):
            l.append(str(x))
        print(str(l))
        c = ["<0 mod 3 | 2 >","<1 mod 3 | 2 >","<2 mod 3 | 2 >"]
        self.assertTrue(l == c)

    def test_SpanInit(self):
        print("Testing spanInit Test Cases: ")
        vals = [DistortedInt(1,5,3), DistortedInt(2,5,3)]
        s = spanInit(vals)
        # expected result:
        r = ["<1 mod 5 | 3 >", "<4 mod 5 | 3 >", "<0 mod 5 | 3 >", "<3 mod 5 | 3 >", "<2 mod 5 | 3 >"]
        self.assertTrue(s == r)

if __name__ == '__main__':
    unittest.main()
