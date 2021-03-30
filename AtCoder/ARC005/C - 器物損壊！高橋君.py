# 2019/07/12

from heapq import heappop,heappush

h,w=map(int,input().split())
w+=2
c=[list('@'*w)]
for _ in range(h):
    c+=[list('@'+input()+'@')]
c+=[list('@'*w)]
h+=2
d=[[float('inf')]*w for _ in range(h)]

xy=[(-1,0),(0,-1),(0,1),(1,0)]

def bfs(s):
    sx,sy=s
    d[sx][sy]=0
    hq=(d[sx][sy],sx,sy)
    que=[]
    heappush(que,hq)
    while que:
        cst,x,y=heappop(que)
        if c[x][y]=='g':break
        for dx,dy in xy:
            nx,ny=x+dx,y+dy
            if c[nx][ny]=='@':continue
            if c[nx][ny]=='#':
                if cst<2:
                    d[nx][ny]=min(d[nx][ny],cst+1)
            else:
                d[nx][ny]=min(d[nx][ny],cst)    

            c[nx][ny]='@'
            hq=(d[nx][ny],nx,ny)
            heappush(que,hq)



for i in range(1,h):
    for j in range(1,w):
        if c[i][j]=='s':s=(i,j)
        if c[i][j]=='g':
            gx=i
            gy=j
bfs(s)

print('NO' if d[gx][gy]==float('inf') else 'YES')
