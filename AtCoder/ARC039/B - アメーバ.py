# 2019/11/20

h,w=map(int,input().split())
b=[list(map(int,input())) for _ in range(h)]
dir=[(-1,0),(0,-1),(0,1),(1,0)]
ans=[[0]*w for _ in range(h)]

def find_min(i,j):
    ret=100
    for dx,dy in dir:
        ret=min(ret,b[i+dx][j+dy])
    return ret

def solve(i,j,ret):
    for dx,dy in dir:
        b[i+dx][j+dy]-=ret
    ans[i][j]+=ret

for i in range(1,h-1):
    for j in range(1,w-1):
        ret=find_min(i,j)
        if ret:solve(i,j,ret)

[print(*e,sep='') for e in ans]