n,a,b=map(int,input().split())
res=(b*(n-1)+a)-(a*(n-1)+b)+1
print(max(0,res))