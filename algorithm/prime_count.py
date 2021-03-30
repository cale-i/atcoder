# n個の個数を列挙する

import itertools as it

class Primes:
    def __init__(self):
        self.primes=it.count(2)
    

    def __iter__(self):
        return self


    def __next__(self):
        p=next(self.primes)
        self.primes=filter(lambda x: x%p!=0,self.primes)
        return p

# 1から100未満の素数
res=list(it.takewhile(lambda x:x<100,Primes()))
print(res)

# 最初の100個の素数
res=list(it.islice(Primes(),100))
print(res)