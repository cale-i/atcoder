# 2019/09/18

n=int(input())
a=list(map(int,input().split()))
cnt=0
minus=0
suma=0
mina=float('inf')
for i in range(n):
    if a[i]<0:
        minus+=1
    suma+=abs(a[i])
    mina=min(mina,abs(a[i]))

ans=suma
if minus%2 and 0 not in a:
    ans-=mina*2
print(ans)