# 2019/07/29

x,y=map(int,input().split())

if y%2==1:
    print(-1)
    exit()

cnt=y//2
if -cnt<=x<=cnt and x%2==cnt%2:print(cnt)
else:print(-1)