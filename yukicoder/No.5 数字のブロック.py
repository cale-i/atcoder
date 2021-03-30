# 2019/12/28

l=int(input())
n=int(input())
w=sorted(map(int,input().split()))
cnt=0
ans=0
for e in w:
    if cnt+e>l:break
    cnt+=e
    ans+=1
print(ans)