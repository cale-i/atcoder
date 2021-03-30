# 2019/06/27
# 幅優先探索 BFS
from collections import deque

h,w=map(int,input().split())
sy,sx=map(int,input().split())
sy-=1
sx-=1
gy,gx=map(int,input().split())
gy-=1
gx-=1
que=deque()
c=[]
for i in range(h):
   c+=[list(input())] 
'''
for i in range(h):
    print(*c[i])
'''
def bfs(y,x):
    c[y][x]=0
    que.append((y,x))
    yx=[(-1,0),(0,-1),(0,1),(1,0)]

    while que:
        y,x=que.popleft()
        if y==gy and x==gx:return c[y][x]
        for dy,dx in yx:
            ny=y+dy
            nx=x+dx
            if c[ny][nx]=='.':
                que.append((ny,nx))
                c[ny][nx]=int(c[y][x])+1
            


res=bfs(sy,sx)
print(res)
