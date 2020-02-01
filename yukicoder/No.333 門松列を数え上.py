# yukicoder No.333 門松列を数え上 2020/02/02

a,b=map(int,input().split())
lim=2*10**9
ans=0
if a>b:
    ans+=(a-b-1)
    ans+=lim-a
else:
    ans+=(a-1)
    ans+=(b-a-1)
print(ans)