# 2019/12/08

num=4_000_000
a=1
b=2
c=a+b

cnt=2
while c<=num:
    c=a+b
    a,b=b,c
    if c%2==0:cnt+=c
print(cnt)