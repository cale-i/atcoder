# # 2020/01/10

# from fractions import gcd

# n,m=map(int,input().split())
# a=list(map(int,input().split()))

# aa=list(map(lambda x: x//2,a))
# l=aa[-1]
# g=0
# for i in range(len(aa)-1):
#     g=gcd(g,aa[i])
# lcm=(l*g)//gcd(l,g)

# print(-(-m//lcm//2) if m>=lcm else 0)

# 2020/01/10

from fractions import gcd

n,m=map(int,input().split())
a=list(map(int,input().split()))

aa=list(map(lambda x: x//2,a))
lcm=aa.pop()
for e in aa:
    lcm=(lcm*e)//gcd(lcm,e)
    
print(-(-m//lcm//2) if m>=lcm else 0)
