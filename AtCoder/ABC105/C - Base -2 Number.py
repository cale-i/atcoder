# 2019/08/16

n=int(input())
ans=''
res=-n
if n==0:
    print(0)
    exit()

while res:
    ans=str(abs(res%-2))+ans
    res//=-2

print(ans)