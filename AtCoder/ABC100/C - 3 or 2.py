# 2019/07/19

n=int(input())
a=list(map(int,input().split()))

cnt=0
for i in range(n):
    res=a[i]
    while res%2==0:
        res//=2
        cnt+=1
print(cnt)
 