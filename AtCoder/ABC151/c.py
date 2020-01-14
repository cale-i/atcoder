# 2020/01/12

n,m=map(int,input().split())
ps=[0]*(n+1)
ac=0
wa=0

for i in range(m):
    p,s=input().split()
    p=int(p)
    if ps[p]>0:continue
    if s=='WA':
        ps[p]-=1
    else:
        wa+=-ps[p]
        ps[p]=1
        ac+=1
print(*[ac,wa])