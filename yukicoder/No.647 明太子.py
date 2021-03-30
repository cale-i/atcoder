# yukicoder No.647 明太子 2020/01/25

n=int(input())
ab=[tuple(map(int,input().split())) for _ in range(n)]
m=int(input())
xy=[tuple(map(int,input().split())) for _ in range(m)]

ans=[0]*m
MAX=0
for i in range(m):
    x,y=xy[i]
    for a,b in ab:
        if x<=a and b<=y:
            ans[i]+=1
            MAX=max(MAX,ans[i])
if MAX==0:
    print(0)
    exit()

for i in range(m):
    if ans[i]==MAX:
        print(i+1) 