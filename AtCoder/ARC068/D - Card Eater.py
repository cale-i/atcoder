# 2019/09/09

from collections import Counter

n=int(input())
C=Counter(list(map(int,input().split())))

even=0
odd=0
ans=len(C)
for k,v in C.items():
    if v>1:
        if v%2:
            odd+=1
        else:
            even+=1

if even%2:
    ans-=1

print(ans)
