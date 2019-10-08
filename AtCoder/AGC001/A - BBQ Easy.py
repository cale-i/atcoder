# 2019/08/15

n=2*int(input())
l=sorted(list(map(int,input().split())))
cnt=0
for i in range(0,n,2):
    cnt+=min(l[i],l[i+1])
print(cnt)


# 2019/06/05

n=int(input())
l=sorted(map(int,input().split()))
ans=0
while len(l)>1:
    ans+=min(l.pop(),l.pop())
print(ans)
