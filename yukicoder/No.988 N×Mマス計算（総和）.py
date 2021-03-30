# yukicoder No.988 N×Mマス計算（総和） 2020/03/09

n,m,k=map(int,input().split())
op,*b=input().split()
b=[int(e) for e in b]
a=[int(input()) for _ in range(n)]
sum_b=sum(b)

def solve(op):
    ans=0
    if op=='+':
        for e in a:
            ans+=sum_b+e*m
            ans%=k
    else:
        for e in a:
            ans+=sum_b*e
            ans%=k
    return ans

ans=solve(op)
print(ans)