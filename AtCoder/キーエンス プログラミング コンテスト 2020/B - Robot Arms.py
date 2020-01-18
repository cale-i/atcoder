# 2020/01/19

import sys
input=sys.stdin.readline

n=int(input())

xl=[]
for i in range(n):
    x,l=map(int,input().split())
    xl.append((max(0,x-l),x+l))

xl.sort(key=lambda x: x[1])

pre_x=xl[0][1]

cnt=0
for i in range(1,n):
    if xl[i][0]<pre_x:
        cnt+=1
    else:
        pre_x=xl[i][1]
print(n-cnt)