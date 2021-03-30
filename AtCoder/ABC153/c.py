n,k=map(int,input().split())
h=sorted(list(map(int,input().split())),reverse=True)
ans=sum(h[k:])
print(ans)