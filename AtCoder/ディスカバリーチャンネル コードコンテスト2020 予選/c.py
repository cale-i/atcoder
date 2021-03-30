h,w,k=map(int,input().split())
g=[[0]*(w+2)]
for i in range(h):
    g+=[[0]+list(input())+[0]]
g+=[[0]*(w+2)]

for i in range(1,h+1):
    for j in range(1,w+1):
        cnt=0
        if g[i][j]=='#':cnt=+1
        dx,dy=i,j
        r,d=0,0
        while cnt<2:
            
