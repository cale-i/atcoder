# 2019/09/28

n=int(input())

def diviser(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print('YES' if diviser(n) else 'NO')