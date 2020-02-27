class DistortedInt:
    def __init__(self, obj, n, alpha):
        self.object = obj
        self.alpha = alpha
        self.n = n
# overwrite "print"
    def __str__(self):
        return "< "+str(self.object)+" mod "+str(self.n)+" | "+str(self.alpha)+" >"
# define "*"
    def __mul__(self,other):
        if (self.alpha == other.alpha) & (self.n == other.n):
            return DistortedInt((self.alpha*self.object + (1-self.alpha)*other.object)%(self.n), self.n, self.alpha)
        else:
            print("Values must share 'n' and 'alpha' values")
        # return DistortedInt(2*self.object-other.object)
    def __eq__(self,other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self,other):
        return not self.__eq__(other)

# Still to implement:
# # make sure input is valid
# # n is negative?
# # if obj or alpha NOT in Z_n

# needs to be tested more, but works as far as I can tell
def HasDistortedIdempotentProperty(n,a):
    check = True
    for i in range(1,n):
        q = DistortedInt(i,n,a)
        if q*q != q:
            check = False
    return check

# returns the empty list for n=1, a=0, this should not happen
def DistortedRootsOfOne(n,a):
    lst = []
    for i in range(1,n):
        q = DistortedInt(i,n,a)
        if q*q == DistortedInt(1,n,a):
            lst.append(str(q))
    return lst

if __name__ == "__main__":
    for i in range(1,10):
        for j in range(i):
            print(DistortedRootsOfOne(i,j))
