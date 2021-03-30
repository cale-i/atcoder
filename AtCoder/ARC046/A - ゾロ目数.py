# 2019/10/01

n=int(input())

d=n//9+1
c=n%9
if c:
    print(int(str(c)*d))
else:
    print(int(str(9)*(d-1)))