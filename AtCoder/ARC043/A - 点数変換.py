# 2019/10/30

n,a,b=map(int,input().split())
s=[int(input()) for _ in range(n)]

maxs=max(s)
mins=min(s)
if maxs==mins:
    print(-1)
    exit()
p=b/(max(s)-min(s))
q=a-(sum(s)*p/n)
print(*[p,q])