# 2019/11/3

x,y=map(int,input().split())
k=int(input())

x+=min(k,y)
k-=min(k,y)
if k>0:
    x-=k
print(x)