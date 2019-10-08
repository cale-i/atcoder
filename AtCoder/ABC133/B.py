n,d=map(int,input().split())

x=[]
for i in range(n):
    x+=[list(map(int,input().split()))]

cnt=0

for i in range(n):
    for j in range(i+1,n):
        res=0
        for xa,xb in zip(x[i],x[j]):
            res+=abs(xa-xb)**2

        tmp=int(res**0.5)
        if int(tmp**2)==res:
            cnt+=1

print(cnt)