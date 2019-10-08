# 2019/08/15

n=int(input())
x=list(map(int,input().split()))

res=float('inf')
for y in range(min(x),max(x)+1):
    cnt=0
    for i in range(n):
        cnt+=(x[i]-y)**2
    res=min(res,cnt)
print(res)