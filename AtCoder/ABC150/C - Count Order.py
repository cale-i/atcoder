# 2020/01/10

from itertools import permutations

n=int(input())
p=tuple(map(int,input().split()))
q=tuple(map(int,input().split()))

P=sorted(list(permutations(range(1,n+1))))


ans=0
for idx,e in enumerate(P,1):
    if e==p:
        ans+=idx
    if e==q:
        ans-=idx
    
print(abs(ans))