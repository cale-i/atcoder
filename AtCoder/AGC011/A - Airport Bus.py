# 2019/06/01

n,c,k=map(int,input().split())
t=[]
for i in range(n):
    t.append(int(input()))
t.sort()

tmp=t[0]
ans=0
cnt=1

for i in range(1,n):
    if t[i]>tmp+k or cnt>=c:
        tmp=t[i]
        cnt=1
        ans+=1
    else:cnt+=1
ans+=1
print(ans)
