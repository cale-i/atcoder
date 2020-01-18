# 2020/01/18

q=int(input())

def solve(n,K):
    i=0
    res=0
    if k==1:
        return n-1
    while n>res:
        res+=k**i
        i+=1
    return i-1

for i in range(q):
    n,k=map(int,input().split())
    print(solve(n,k))