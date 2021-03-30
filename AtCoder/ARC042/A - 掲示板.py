# 2019/10/30

n,m=map(int,input().split())
a=[int(input()) for _ in range(m)][::-1]
used=set()
res=[]
for e in a:
    if e in used:continue
    res.append(e)
    used.add(e)
if len(res)<n:
    res+=set(range(1,n+1))^used
print(*res,sep='\n')
