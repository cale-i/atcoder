# 2019/11/19

h,w,d=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]
ans=0


def solve(gx,gy):
    res=0
    sx,sy=0,0
    dst=gx-sx+gy-sy
    if dst%2==d%2 and dst<=d:
        res=a[gx][gy]
    return res 


for i in range(h):
    for j in range(w):
        ans=max(ans,solve(i,j))
print(ans)