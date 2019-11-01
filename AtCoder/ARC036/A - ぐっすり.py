# 2019/10/28

n,k=map(int,input().split())
t=[int(input()) for i in range(n)]

for i in range(2,n):
    if t[i-2]+t[i-1]+t[i]>=k:continue
    print(i+1)
    exit()
else:print(-1)