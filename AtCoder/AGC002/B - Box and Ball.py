# 2019/09/06

n,m=map(int,input().split())
box=[[1,1,0]]+[[1,0,1] for _ in range(n-1)]

for i in range(m):
    x,y=map(int,input().split())
    x-=1;y-=1
    box[y][1]|=box[x][1]
    box[y][2]|=box[x][2]
    box[y][0]+=1
    box[x][0]-=1
    if box[x][0]==0:
        box[x]=[0,0,0]        

cnt=0
for c,r,w in box:
    if  not c:continue
    if r:
        cnt+=1
print(cnt)
    