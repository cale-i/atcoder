# 2019/09/06

n=int(input())
p=[0]+list(map(int,input().split()))

cnt=0
for i in range(1,n+1):
    if i!=p[i]:continue
    if i==n:p[i],p[i-1]=p[i-1],p[i]
    else:
        p[i],p[i+1]=p[i+1],p[i]
    cnt+=1
    
print(cnt)