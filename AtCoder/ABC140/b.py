# 2019/09/07

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[0]+list(map(int,input().split()))

cnt=sum(b)
for i in range(n-1):
    if a[i]+1==a[i+1]:
        cnt+=c[a[i]]
    
print(cnt)