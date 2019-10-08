# 2019/09/03

n,a,b=map(int,input().split())
x=list(map(int,input().split()))

cnt=0
for i in range(n-1):
    cnt+=min(abs(x[i]-x[i+1])*a,b)
print(cnt)