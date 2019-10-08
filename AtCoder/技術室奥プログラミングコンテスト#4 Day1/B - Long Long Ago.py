# 2019/07/28

from bisect import bisect_left

n,k=map(int,input().split())
a=list(map(int,input().split()))
A=sorted(a)

if A[0]>k:
    print(-1)
    exit()
print(1+a.index(A[bisect_left(A,k)-1]))

