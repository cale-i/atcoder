# 2019/10/26

a,b=map(int,input().split())
n_even=(b//2)-(a-1)//2

if (b-a+1)%2:
    if a%2:
        print(a^(n_even%2))
    else:
        print(b^((n_even-1)%2))
else:
    if a%2:
        print(a^b^((n_even-1)%2))
    else:
        print(n_even%2)