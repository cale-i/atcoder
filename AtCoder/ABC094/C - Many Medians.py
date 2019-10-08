# 2019/08/08

from bisect import bisect_left,bisect_right

n=int(input())
x=list(map(int,input().split()))
xx=sorted(x)
mid=n//2

for i in range(n):
    if bisect_left(xx,x[i])<mid:
        print(xx[mid])
    else:
        print(xx[mid-1])


# ちょっと変更
# 2019/08/08
from bisect import bisect_left,bisect_right

n=int(input())
x=list(map(int,input().split()))
xx=sorted(x)
mid=n//2

ans=[]
for i in range(n):
    if bisect_left(xx,x[i])<mid:
        ans.append(xx[mid])
    else:
        ans.append(xx[mid-1])
print(*ans,sep='\n')