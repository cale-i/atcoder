n=int(input())
a=list(map(int,input().split()))[::-1]
b=list(map(int,input().split()))[::-1]

cnt=0

for i in range(n):
    for j in range(2):
        x=a[i+j]
        y=b[i]
        m=min(x,y)
        b[i]-=m
        a[i+j]-=m
        cnt+=m

print(cnt)