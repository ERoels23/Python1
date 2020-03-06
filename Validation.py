'''
Custom Exceptions and methods to validate user input regarding DistortedInts
'''

# Exception for bad DistortedInt instantiation
class InvalidArgumentException(Exception):
    pass

# Exception for bad DistortedInt multiplication
class InvalidOperandException(Exception):
    pass


# Method used by DistortedInt init. to ensure valid arguments
def ValidateArguments(x, n, alpha):
    if not __validation(x, n, alpha):
        raise InvalidArgumentException

# Privately used method to check all cases and return True or False
def __validation(x, n, alpha):
    # Verify all arguments are integers
    if not (isinstance(x, int) and isinstance(n, int) and isinstance(alpha, int)):
        return False

    # Verify n is positive integer
    if n < 1:
        return False

    # Verify that both the underlying integer x and alpha are in set Zn
    if not (x in range(n) and alpha in range(n)):
        return False

    # Otherwise, all arguments valid and return True
    return True


# Method to validate DistortedInts are defined for same underlying int and alpha
def ValidateOperands(x, y):
    if not (x.alpha == y.alpha) & (x.n == y.n):
        raise InvalidOperandException
