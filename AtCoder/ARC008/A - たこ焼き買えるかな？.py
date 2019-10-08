# 2019/09/14

n=int(input())

a=n//10
b=n%10
ans=min(a*100+b*15,-(-n//10)*100)
print(ans)
