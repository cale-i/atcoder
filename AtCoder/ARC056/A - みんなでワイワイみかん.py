# 2019/09/23
"""
a,b,k,l=map(int,input().split())

cnt=0
while k*a>=b:
    cnt+=b
    k-=l
cnt+=max(k*a,0)
print(cnt)
"""

a,b,k,l=map(int,input().split())

n=(k//l)*b+(k%l)*a
m=-(-k//l)*b
print(min(n,m))