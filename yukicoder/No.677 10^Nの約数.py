# yukicoder No.677 10^Nの約数 2020/01/25

n=int(input())

ans=set()
for i in range(n+1):
    for j in range(n+1):
        ans.add(2**i*5**j)
ans=sorted(ans)
print(*ans,sep='\n')