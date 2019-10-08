# 2019/08/15

a,b,c=sorted(map(int,input().split()))

if a%2 and b%2 and c%2:
    ans=a*b
else:
    ans=0

print(ans)