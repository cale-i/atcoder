# 2019/10/22

l,x,y,s,d=map(int,input().split())

if s>d:
    dist=d+l-s
else:
    dist=d-s
cw=dist/(x+y)
ccw=0
if y!=x:
    ccw=max((l-dist)/(y-x),0)
if s==d:print(0)
elif ccw==0:
    print(cw)
elif cw==0:
    print(ccw)
else:print(min(cw,ccw))