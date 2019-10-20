n=int(input())
d=list(map(int,input().split()))

cnt=0
for i in range(n):
    for j in range(i,n):
        if i==j:continue    
        cnt+=d[i]*d[j]
print(cnt)