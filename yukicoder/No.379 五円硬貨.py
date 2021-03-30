# yukicoder No.379 五円硬貨 2020/01/31

from decimal import getcontext,Decimal

n,g,v=map(int,input().split())
go=n//5
getcontext().prec=30
dec=Decimal(g*go)/Decimal(v)
print(dec)