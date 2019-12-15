# 2019/12/10

for a in range(1001):
    for b in range(a+1,1001):
        c=1000-(a+b)
        if c<=b:break
        if a**2+b**2==c**2:
            print(a*b*c)