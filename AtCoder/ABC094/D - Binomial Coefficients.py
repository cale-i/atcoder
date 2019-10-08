# 2019/09/06
# パスカルの三角形

from bisect import bisect_left

n=int(input())
*a,mxv=sorted(list(map(int,input().split())))

mid=mxv//2

r=bisect_left(a,mid) 
if r>=n-1:
    r=0
l=r-1 if r else 0

ans=[mxv]

if abs(mxv/2-a[r])>abs(mxv/2-a[l]):
    ans.append(a[l])
else:
    ans.append(a[r])
print(*ans)