# 2019/07/30
#Pypy3

n,m=map(int,input().split())

a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
b=[]
for i in range(n):
    b.append(list(map(int,input().split())))

cnt=min(b[0])

for i in range(1,n):
    c=[]
    for j in range(m):
        k=1
        while k*a[i][j]<cnt:
            k+=1
        a[i][j]*=k
        c.append(a[i][j]-cnt+b[i][j])
    cnt+=min(c)

print(cnt)