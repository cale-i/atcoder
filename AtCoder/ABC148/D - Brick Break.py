# 2019/12/22

n=int(input())
a=list(map(int,input().split()))
counter=1
ans=0
for i in range(n):
    if a[i]==counter:
        counter+=1
        continue
    ans+=1

print(-1 if ans==n else ans)