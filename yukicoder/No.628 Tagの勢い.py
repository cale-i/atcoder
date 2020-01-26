# yukicoder No.628 Tagの勢い 2020/01/26

n=int(input())
tags=dict()

for i in range(n):
    no=int(input())
    m,s=map(int,input().split())
    tag=list(input().split())
    for t in tag:
        tags[t]=tags.get(t,0)+s

res=sorted(tags.items(),key=lambda x: (-x[1],x[0]))

lim=min(len(res),10)
for i in range(lim):
    print(*res[i])