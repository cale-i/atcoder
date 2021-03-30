# 2019/12/30

from itertools import combinations

n=int(input())
pq=[]
for i in range(n):
    p,q=map(int,input().split())
    pq.append([p,q])

cnt=0
for c in list(combinations(pq,3)):
    s=abs((c[1][0]-c[0][0])
         *(c[2][1]-c[0][1])
         -(c[1][1]-c[0][1])
         *(c[2][0]-c[0][0])
    )   
    ss=s//2
    if ss*2==s and s:
        cnt+=1
print(cnt)