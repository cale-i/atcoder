# 2019/10/29

k=int(input())


def rev_gcd(a,b,k):
    if k:
        rev_gcd(a+b,a,k-1)
    else:
        print(*(a,b))
        exit()


rev_gcd(2,1,k-1)