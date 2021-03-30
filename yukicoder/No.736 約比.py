# yukicoder No.736 約比 2020/01/23

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

            
n=int(input())
a=list(map(int,input().split()))


_gcd=GCD(a)

ans=list(map(lambda x: str(x//_gcd.gcd),a))
print(':'.join(ans))