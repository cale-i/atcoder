# 2019/09/16

import sys
input=sys.stdin.readline

n,h=map(int,input().split())

que=[]

for i in range(n):
    a,b=map(int,input().split())
    que.append((a,b))

que.sort(key=lambda x: (x[0],x[1]))
a,b=que.pop()
que.sort(key=lambda x: x[1])

cnt=0
def solve(cnt,h):
    while h>0 and que:
        _,bb=que.pop()
        if h<=b:
            break
        if bb>=a:
            h-=bb
            cnt+=1
        else:
            break
    return cnt,h

if que:
    cnt,h=solve(cnt,h)



if h>0:
    h-=b
    cnt+=1
if h>0:
    cnt+=-(-h//a)
print(cnt)