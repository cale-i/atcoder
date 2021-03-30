# 2019/08/14
# 変な計算してた

"""
n=int(input())
T,A=map(int,input().split())
for i in range(n-1):
    p,q=map(int,input().split())
    
    qtmp=1
    if q<A:
        qtmp=(-(-(A-q)//q)+1)*q
        q=
    if A%q==0:b=0
    else:b=q-(A%q)

    a=(A+b)*p//q-T
    if p<T:
        ptmp=(-(-(T-p)//p)+1)*p
        a=ptmp-T
    T+=a
    A+=b
print(T+A)
"""
# かんにんぐ
n=int(input())

a,b=1,1
for _ in range(n):
    x,y=map(int,input().split())
    m=max(-(-a//x),-(-b//y))
    a=x*m
    b=y*m
print(a+b)