# https://atcoder.jp/contests/abc094/tasks/abc094_b

n,m,x=map(int,input().split())
a=list(map(int,input().split()))
left=0
for i in range(m):
    if a[i]<x:left+=1
    else:break
right=m-left
print(min(left,right))