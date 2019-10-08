# 2019/09/30

n=int(input())


def is_prime(n):
    if n==1:return False
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i:continue
        return False
    return True


def is_poi(n):
    if n==1:return False
    if n%2 and n%5 and n%3:
        return True
    else:
        return False


if is_prime(n) or is_poi(n):
    print('Prime')
else:
    print('Not Prime')
    
