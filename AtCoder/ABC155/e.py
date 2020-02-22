n=list(str(input()))

ans=0
for e in n:
    a=int(e)
    b=10-(a)+1
    ans+=min(a,b)
print(ans)
    