# yukicoder No.178 美しいWhitespace (1) 2020/02/04

n=int(input())
ab=[]
mx=0
for i in range(n):
    a,b=map(int,input().split())
    ab.append((a,b))
    mx=max(mx,a+4*b)

is_odd=True if ab[0][0]%2 else False
ans=0

for a,b in ab:
    if a%2!=is_odd:
        print(-1)
        exit()
    ans+=mx-(a+4*b)
print(ans//2)