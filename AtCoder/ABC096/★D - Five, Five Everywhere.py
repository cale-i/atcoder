# 2019/12/13
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


n=int(input())

res=list(it.islice(Primes(),n+1))
print(*res[1:])