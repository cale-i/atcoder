# 2019/07/31

from fractions import gcd

n=int(input())
a=list(map(int,input().split()))

g1=[0]*n
g2=[0]*n
g1[0]=a[0]
g2[-1]=a[-1]


i=1
j=n-2
while i<n and j>-1:
    g1[i]=gcd(g1[i-1],a[i])
    g2[j]=gcd(g2[j+1],a[j])
    i+=1;j-=1

ans=[0]*n
ans[0]=g2[1]
ans[-1]=g1[-2]

for i in range(1,n-1):
    ans[i]=gcd(g2[i+1],g1[i-1])

print(max(ans))