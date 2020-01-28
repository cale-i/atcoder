# yukicoder No.521 Cheeses and a Mousetrap 2020/01/28

n,k=map(int,input().split())

if not 0<k<=n:
    print(0)
    exit()

if n%2 and (n//2+1)==k:
    ans=n-1
else:
    ans=n-2

print(ans)