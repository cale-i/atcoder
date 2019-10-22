# 2019/10/22

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a)<sum(b):
    print(-1)
    exit()
plus=[]
minus=[]
for aa,bb in zip(a,b):
    if aa==bb:continue
    if aa>bb:plus.append(aa-bb)
    else:minus.append(bb-aa)

plus.sort()
minus.sort(reverse=True)
p=0
m=sum(minus)
cnt=len(minus)
p=0
while p<m:
    p+=plus.pop()
    cnt+=1
print(cnt)
