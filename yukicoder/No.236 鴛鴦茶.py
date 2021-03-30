# yukicoder No.236 鴛鴦茶 2020/02/03

a,b,x,y=map(int,input().split())
xa=x/a
yb=y/b

if a==b:
    ans=2*min(x,y)
else:
    ans=(a+b)*min(xa,yb)
print(ans)