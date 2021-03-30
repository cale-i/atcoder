# 2019/08/26
n=int(input())
ng=sorted([int(input()) for _ in range(3)])
if n in ng:
    print('NO')
    exit()

cnt=100
while n or cnt:
    if n-3 not in ng and n>=3:
        n-=3
    elif n-2 not in ng and n>=2:
        n-=2
    elif n-1 not in ng and n>=1:
        n-=1
    else:
        print('NO')
        exit()
    cnt-=1
    if n==0:break
    if n and cnt==0:
        print('NO')
        exit()
print('YES')
