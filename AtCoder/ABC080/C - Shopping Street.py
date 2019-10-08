# 2019/08/15

n=int(input())
f=[[]]*n
for i in range(n):
    f[i]=int(input().replace(' ',''),2)

p=[[]]*n
for i in range(n):
    p[i]=list(map(int,input().split()))

res=float('-inf')
for i in range(1,2**10):
    cnt=0
    for j in range(n):
        idx=bin(i&f[j]).count('1')
        cnt+=p[j][idx]
    res=max(res,cnt)
print(res)