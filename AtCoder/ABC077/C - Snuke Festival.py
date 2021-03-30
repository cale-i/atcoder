# 2019/09/07

from bisect import bisect_left,bisect_right

n=int(input())
a=sorted(list(map(int,input().split())))
b=list(map(int,input().split()))
c=sorted(list(map(int,input().split())))

cnt=0
for bb in b:
    aa=bisect_left(a,bb)
    cc=n-bisect_right(c,bb)
    cnt+=aa*cc
print(cnt)
