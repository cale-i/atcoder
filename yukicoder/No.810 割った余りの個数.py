# yukicoder No.810 割った余りの個数 2020/01/21

l,r,m=map(int,input().split())
if r-l>=m:
    ans=m
else:
    ans=(r+1)-l
print(ans)