# 2019/12/24

n,m=map(int,input().split())
cnt=0
for i in range(1,n+1):
    cnt+=(i**2)%m
print(cnt%m)