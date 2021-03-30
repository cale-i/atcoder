# 2019/08/12
import sys

input=sys.stdin.readline

n=int(input())
a=[0]*n
b=[0]*n
for i in range(n):
    aa,bb=map(int,input().split())
    a[i]=aa%bb
    b[i]=bb

cnt=0
for i in range(n-1,-1,-1):
    res=(cnt+a[i])%b[i]
    if res:cnt+=b[i]-res
    
print(cnt)