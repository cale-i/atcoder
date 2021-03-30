# yukicoder No.146 試験監督（1） 2020/02/12

MOD=10**9+7
n=int(input())
ans=0
for _ in range(n):
    c,d=map(int,input().split())
    ans+=-(-c//2)*d
    ans%=MOD
print(ans)