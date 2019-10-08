# 2019/09/01

a,b=map(int,input().split())

cnt=a
if b==1:
    print(0)
    exit()
ans=1
while True:
    if cnt>=b:break
    cnt+=a-1
    ans+=1
print(ans)