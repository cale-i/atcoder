# 2019/08/09

n=int(input())
a=sorted(list(map(int,input().split())))
r=3*n-1
cnt=0
for l in range(n):
    cnt+=a[r-1]
    r-=2
print(cnt)