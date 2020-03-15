d,n=map(int,input().split())
ans=n*100**d
if n!=100:
    print(ans)
else:
    print(ans+1*100**d)