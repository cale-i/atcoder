# 2019/10/11
# 符号付面積:S=|ad-bc|//2 ※(x1,y1),(x2,y2),(x3,y3)=(0,0),(a,b),(c,d)



xy=list(map(int,input().split()))
x,y=[],[]

xx=xy[0]
yy=xy[1]
for i in range(6):
    if i%2:y.append(xy[i]-yy)
    else:x.append(xy[i]-xx)

S=abs(x[1]*y[2]-y[1]*x[2])/2
print(S)