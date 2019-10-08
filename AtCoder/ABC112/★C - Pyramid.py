# 2019/07/26
# やりなおし

n=int(input())

xyh=[]

for i in range(n):
    x,y,h=map(int,input().split())
    xyh.append((h,x,y))

xyh.sort(reverse=True)

for i in range(101):
    for j in range(101):
        
        H=xyh[0][0]+abs(xyh[0][1]-i)+abs(xyh[0][2]-j)
        for k in range(1,n):
            h,x,y=xyh[k]
            HH=h+abs(x-i)+abs(y-j)
            if H==HH or H-HH<0 and h==0:continue
            else:break
        else:
            print(*[i,j,H])
            exit()  