n=int(input())
x=list(map(int,input().split()))

avg1=sum(x)//n
avg2=avg1+1

cnt1=0
cnt2=0
for i in range(n):
    cnt1+=(x[i]-avg1)**2
    cnt2+=(x[i]-avg2)**2
print(min(cnt1,cnt2))