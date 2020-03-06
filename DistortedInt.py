from Validation import *


class DistortedInt:
    '''
    encapsulates a Distorted Integer <object mod n | alpha>
    where x*y = (a*x + (1-a)*y)%n
    '''
    def __init__(self, obj, n, alpha):
        '''
        Construct a new 'DistortedInt' object.

        :param obj: the object of the DistortedInt
        :param n: the modulus of the DistortedInt
        :param alpha: the distortion of the DistortedInt
        '''

        try:
            ValidateArguments(obj, n, alpha)
            self.object = obj
            self.alpha = alpha
            self.n = n
        except InvalidArgumentException:
            print("Invalid arguments given\n{ modulus 'n' > x, alpha >= 0 }")
        except Exception as e:
            print(e)

    # overwrite "print"
    def __str__(self):
        '''
        returns a string representation of a DistortedInt object
        '''
        return "<"+str(self.object)+" mod "+str(self.n)+" | "+str(self.alpha)+" >"

    # define "*"
    def __mul__(self, other):
        '''
        redefines multiplication according to DistortedInt Multiplication
        where x*y = (a*x + (1-a)*y)%n
        '''
        # if (self.alpha == other.alpha) & (self.n == other.n):
        #     return DistortedInt((self.alpha*self.object + (1-self.alpha)*other.object) % self.n, self.n, self.alpha)
        # else:
        #     print("Values must share 'n' and 'alpha' values")
        try:
            ValidateOperands(self, other)
            return DistortedInt((self.alpha * self.object + (1 - self.alpha) * other.object) % self.n, self.n, self.alpha)
        except InvalidOperandException:
            print("Operands must be defined for same modulus 'n' and distortion 'alpha'.")

    def __eq__(self,other):
        return isinstance(other, self.__class__) and self.alpha == other.alpha and self.n == other.n and self.object == other.object


def HasDistortedIdempotentProperty(n,a):
    # range of Zn (ex. Z1 = {0} as provided in spec)
    for i in range(n):
        q = DistortedInt(i,n,a)
        if q*q != q:
            return False
    return True

# returns the empty list for n=1, a=0, this should not happen, come back to
def DistortedRootsOfOne(n,a):
    lst = []
    for i in range(n):
        q = DistortedInt(i,n,a)
        if q*q == DistortedInt(1,n,a):
            lst.append(q*q)
    return lst

def IsCommutativeDistortedMultiplication(n, alpha):
    for x in range(n):
        # avoids redundant checks ex. if 0*1 = 1*0, don't need to check 1*0 = 0*1
        for y in range(x,n):
            first = DistortedInt(x, n, alpha)
            second = DistortedInt(y,n,alpha)
            if (first*second != second*first):
                return False
    return True

def IsAssociativeDistortedMultiplication(n, alpha):
    for x in range(n):
        first = DistortedInt(x,n,alpha)
        for y in range(x,n):
            second = DistortedInt(y,n,alpha)
            for z in range(y,n):
                third = DistortedInt(z,n,alpha)
                if (((first*second)*third) != (first*(second*third))):
                    return False
    return True

def IsQuasiDistributiveDistortedMultiplication(n, alpha):
    for x in range(n):
        for y in range(n):
            for z in range(n):
                xD = DistortedInt(x, n, alpha)
                yD = DistortedInt(y, n, alpha)
                zD = DistortedInt(z, n, alpha)
                if (((xD*yD)*zD) != ((xD*yD)*(xD*zD))):
                    return False
    return True

# main for testing purposes...
if __name__ == "__main__":
    print("testing is done within the Testing.py document")
