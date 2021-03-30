# 2019/09/09
# いもす法

from itertools import accumulate
n=int(input())
ab=[]
MAX=0
for i in range(n):
    a,b=map(int,input().split())
    MAX=max(MAX,b)
    ab.append((a,b))

res=[0]*(MAX+2)

for a,b in ab:
    res[a]+=1
    res[b+1]-=1

acc=accumulate(res)

print(max(acc))