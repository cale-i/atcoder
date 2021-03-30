from functools import reduce
try:
    from math import gcd
except:
    from fractions import gcd

class GCD:
    def __init__(self,arg):
        if type(arg) in [list,tuple]:
            self.arr=arg

        self.gcd=self.gcd_list(self.arr)

    def gcd_list(self,arr):
        return reduce(gcd,arr)

    def __repr__(self):
        return repr(self.gcd)

            
arr=[2,4,6,18]

print(GCD(arr))
