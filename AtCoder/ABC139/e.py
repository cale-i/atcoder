# 2019/09/01

n=int(input())

g=[[0]*n for _ in range(n)]

a=[]
for i in range(n):
    a.append(tuple(map(lambda x: int(x)-1,input().split())))


i=0
for e in a:
    cnt=1
    for que in e:
        cnt=min(max(g[i][que],g[que][i]),cnt)
        g[i][que]=cnt
        g[que][i]=cnt
        cnt+=1
    i+=1

ans=0
for e in g:
    ss=set(e)
    if len(ss)!=len(e):
        print(-1)
        exit()
    ans=max(ans,max(e))

print(ans)