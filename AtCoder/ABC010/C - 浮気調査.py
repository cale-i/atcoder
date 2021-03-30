# 2019/09/08

sx,sy,gx,gy,t,v=map(int,input().split())
n=int(input())

for i in range(n):
    cx,cy=map(int,input().split())

    sc=pow((cx-sx)**2+(cy-sy)**2,0.5)
    cg=pow((gx-cx)**2+(gy-cy)**2,0.5)
    dist=sc+cg
    if dist<=t*v:
        print('YES')
        exit()

print('NO')