# 2019/08/08

from math import factorial

n,m=map(int,input().split())
diff=abs(n-m)
if diff>1:ans=0
elif diff==0:
    res=factorial(n)
    ans=2*res%(10**9+7)*res%(10**9+7)
else:
    ans=factorial(n)%(10**9+7)*factorial(m)%(10**9+7)
print(ans)

# 2019/08/08
# 高速改良版
# 10**9+7を取る場合には、factorial時からMODを取ると早い

def mod(n):
    return n%(10**9+7)

def fac(n):
    res=1
    for i in range(1,n+1):
        res=mod(res*i)
    return res

n,m=map(int,input().split())
diff=abs(n-m)
if diff>1:ans=0
elif diff==0:
    ans=mod(2*fac(n)*fac(m))
else:
    ans=mod(fac(n)*fac(m))
print(ans)