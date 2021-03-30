# 2019/08/09

from itertools import accumulate

n=int(input())
a=list(map(int,input().split()))

acc=list(accumulate(a))

ans=float('inf')
for i in range(n-1):
    ans=min(ans,abs(acc[i]-(acc[-1]-acc[i])))
    
print(ans)