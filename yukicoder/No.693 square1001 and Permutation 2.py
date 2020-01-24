# yukicoder No.693 square1001 and Permutation 2 2020/01/25

from heapq import heappop,heapify,heappush

n=int(input())
a=list(map(int,input().split()))
heapify(a)

i=0
ans=0
while a:
    i+=1
    tmp=heappop(a)
    if i==tmp:continue
    else:
        ans+=abs(i-tmp)
print(ans)