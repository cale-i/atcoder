# 2019/08/19

n=int(input())
bxy=[[] for _ in range(n+1)]
for i in range(n):
    x,y=map(int,input().split())
    bxy[x].append(y)

rxy=[[] for _ in range(n+1)]
for i in range(n):
    x,y=map(int,input().split())
    rxy[x].append(y)

print(*bxy)
print(*rxy)