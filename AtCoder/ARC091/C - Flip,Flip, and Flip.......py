# 2019/07/23

n,m=map(int,input().split())

if n>=3 and m>=3:
    print((n-2)*(m-2))
elif n==2 or m==2:
    print(0)
else:
    if n==1 and m==1:print(1)
    else:print(max(n,m)-2)