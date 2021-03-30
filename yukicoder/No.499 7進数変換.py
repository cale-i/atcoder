# yukicoder No.499 7進数変換 2020/01/29

n=int(input())

ans=[]
while True:
    d,m=divmod(n,7)
    n=d
    ans.append(m)
    if d==0:
        break
print(*ans[::-1],sep='')