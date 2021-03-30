# 2019/08/09

a,b,c=map(int,input().split())
if a==b==c:
    if a%2:
        print(0)
    else:
        print(-1)
    exit()

cnt=0
while a%2==0 and b%2==0 and c%2==0:
    a,b,c=(b+c)//2,(a+c)//2,(a+b)//2
    cnt+=1
print(cnt)