#2019/09/24

n=int(input())
a=[0]+list(map(int,input().split()))

cnt=0
for i,e in enumerate(a):
    if e==a[i] and i==a[e]:
        cnt+=1
print(cnt//2)