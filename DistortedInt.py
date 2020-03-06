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
        self.object = obj
        self.alpha = alpha
        self.n = n

    # overwrite "print"
    def __str__(self):
        '''
        returns a string representation of a DistortedInt object
        '''
        return "< "+str(self.object)+" mod "+str(self.n)+" | "+str(self.alpha)+" >"

    # define "*"
    def __mul__(self,other):
        '''
        redefines multiplication according to DistortedInt Multiplication
        where x*y = (a*x + (1-a)*y)%n
        '''
        if (self.alpha == other.alpha) & (self.n == other.n):
            return DistortedInt((self.alpha*self.object + (1-self.alpha)*other.object) % self.n, self.n, self.alpha)
        else:
            print("Values must share 'n' and 'alpha' values")

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


def TestHasDistortedIdempotentProperty():
    # 1 - 100
    for n in range(1, 101):
        # 0 - (n-1)
        for alpha in range(n):
            if (not HasDistortedIdempotentProperty(n, alpha)):
                return False
    return True

# since 1 is in Zn, start from 2 rather than 1???
def TestDistortedRootsOfOne():
    # 1 - 100
    for n in range(2,101):
        # 0 - (n-1)
        for alpha in range(n):
            if (len(DistortedRootsOfOne(n, alpha)) != 1):
                return False
    return True

def IsCommutativeDistortedMultiplication(n, alpha):
    for x in range(n):
        # avoids redundant checks ex. if 0*1 = 1*0,
        # don't need to check 1*0 = 0*1
        for y in range(x,n):
            first = DistortedInt(x, n, alpha)
            second = DistortedInt(y,n,alpha)
            if (first*second != second*first):
                return False
    return True

def TestIsCommutativeDistortedMultiplication():
    # 1 - 100
    for n in range(1, 101):
        # 0 - (n-1)
        for alpha in range(n):
            if (IsCommutativeDistortedMultiplication(n, alpha) and n % 2 == 0):
                print("n: " + str(n) + "  " + "a: " + str(alpha))
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

def TestIsAssociativeDistortedMultiplication():
    lst = []
    for n in range(1,21):
        for a in range(n):
            if IsAssociativeDistortedMultiplication(n, a):
                lst.append((n,a))
    return lst

def TestIsCommutativeDistortedMultiplication():
    l = []
    # 1 - 100
    for n in range(1, 101):
        # 0 - (n-1)
        for alpha in range(n):
            if IsCommutativeDistortedMultiplication(n, alpha):
                l.append((n,alpha))
    return l

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


def TestIsQuasiDistributiveDistortedMultiplication():
    l = []
    # 1 - 20
    for n in range(1, 21):
        # 0 - (n-1)
        for alpha in range(n):
            if (IsQuasiDistributiveDistortedMultiplication(n, alpha)):
                l.append((n, alpha))
    return l


# main for testing purposes...
if __name__ == "__main__":
    print("Testing Idempotent Property: " + str(TestHasDistortedIdempotentProperty()))
    print("Testing Roots of One: " + str(TestDistortedRootsOfOne()))
    commutativeList = TestIsCommutativeDistortedMultiplication()
    print("Testing Commutative Multiplication: " + str(commutativeList))
    print("Testing all odd modulus Commutative Multiplication: " + str(all(n % 2 != 0 for (n,a) in commutativeList)))
    print("Testing Quasi Distributive Multiplication: " + str(TestIsQuasiDistributiveDistortedMultiplication()))
    print("Testing Associative Distorted Multiplication: " + str(TestIsAssociativeDistortedMultiplication()))
