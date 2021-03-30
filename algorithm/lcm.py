from functools import reduce
try:
    from math import gcd
except:
    from fractions import gcd

class LCM:
    def __init__(self,arg):
        if type(arg) in [list,tuple]:
            self.arr=arg

        self.lcm=self.lcm_list(self.arr)

    def lcm_base(self,x,y):
        return (x*y)//gcd(x,y)

    def lcm_list(self,arr):
        return reduce(self.lcm_base,arr,1)

    def __repr__(self):
        return repr(self.lcm)

            
arr=[2,4,6,18]

print(LCM(arr))
