# 2019/09/28

n=int(input())
a=list(map(int,input().split()))
res=[]
for i,e in enumerate(a,1):
    res.append((i,e))

res.sort(key=lambda x: x[1])

for e in res:
    print(e[0],end=' ')
print()