# 2019/12/23

n=int(input())
if n%2:print(0);exit()
num=10
ans=0
while n>=num:
    ans+=n//num
    num*=5
print(ans)