# 2020/01/12

from copy import deepcopy
import sys
from collections import deque

sys.setrecursionlimit(10**7)


def main():
    dr=[(-1,0),(0,-1),(0,1),(1,0)]

    h,w=map(int,input().split())
    g=[list('#')*(w+2)]
    for _ in range(h):
        g+=[['#']+list(input())+['#']]
    g+=[list('#')*(w+2)]


    def bfs(sx,sy,maze):
        res=0
        x,y=sx,sy
        maze[x][y]=0
        que=deque()
        que.append((x,y))

        while que:
            x,y=que.popleft()
            for dx,dy in dr:
                nx=dx+x
                ny=dy+y
                if maze[nx][ny]=='#':continue
                if maze[nx][ny]!='.' and maze[nx][ny]<=maze[x][y]:continue
                maze[nx][ny]=maze[x][y]+1
                que.append((nx,ny))
                res=max(res,maze[nx][ny])
        return res


    ans=0
    maze=deepcopy(g)

    for i in range(1,h+1):
        for j in range(1,w+1):
            if g[i][j]=='#':continue
            res=bfs(i,j,maze)
            ans=max(res,ans)
            maze=deepcopy(g)
    print(ans)

if __name__ == "__main__":
    main()