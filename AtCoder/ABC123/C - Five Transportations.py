# 2019/08/07

n=int(input())
a=min([int(input()) for _ in range(5)])

ans=5+n//a-1 if n%a==0 else 5+n//a
print(ans)
