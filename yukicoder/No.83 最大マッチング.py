# yukicoder No.83 最大マッチング 2020/03/02

n=int(input())
if n%2:
    ans='7'+'1'*((n-3)//2)
else:
    ans='1'*(n//2)
print(ans)