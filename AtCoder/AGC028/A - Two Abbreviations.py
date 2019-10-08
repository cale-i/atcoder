# 2019/08/11
# listで書いた場合TLEになる

from fractions import gcd

n,m=map(int,input().split())
s=input()
t=input()
lcd=(n*m)//gcd(n,m)
x={}
aa=(lcd//n)
bb=(lcd//m)
for i in range(n):
    a=i*aa
    x[a]=s[i]

for i in range(m):
    b=i*bb
    if b in x and x[b]!=t[i]:
        print(-1)
        exit()
    
print(lcd)

# 2019/08/11
# ↓TLE
from fractions import gcd

n,m=map(int,input().split())
s=list(input())
t=list(input())
lcd=(n*m)//gcd(n,m)
x=['' for _ in range(lcd)]

for i in range(n):
    a=i*(lcd//n)
    x[a]=s[i]

for i in range(m):
    b=i*(lcd//m)
    if x[b]==t[i] or x[b]=='':
        x[b]=t[i]
    else:
        print(-1)
        exit()
    
print(lcd)
