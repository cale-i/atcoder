# yukicoder No.740 幻の木 2020/01/23

n,m,p,q=map(int,input().split())

an=m*12+q*m
ans=12*(n//an)
rest=n-(n//an)*an
month=0
for i in range(1,13):
    if 1<=i<p or (p+q)<=i<=12:
        rest-=m
    elif p<=i<=(p+q-1):
        rest-=2*m
    
    if rest<=0:break
print(ans+i)