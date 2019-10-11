# 2019/10/11

n,k=map(int,input().split())
s=list(input())+[None]

cnt=1
ss=[]
if s[0]=='0':ss.append(0)

i=1
while i<=n:
    if s[i]==s[i-1]:
        cnt+=1
    else:
        ss.append(cnt)
        cnt=1
        
    i+=1

if s[-2]=='0':ss.append(0)
nn=len(ss)
k=min(nn//2,k)
res=sum(ss[:k*2+1])
cnt=res
l=0
for r in range(k*2+2,nn,2):
    cnt-=(ss[l]+ss[l+1])
    cnt+=(ss[r]+ss[r-1])
    res=max(res,cnt)
    l+=2

print(res)

