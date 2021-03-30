# 2019/11/25

n,m=map(int,input().split())
py=[]
for i in range(m):
    p,y=map(int,input().split())
    py.append([p,y,i])
py.sort(key=lambda x:(x[0],x[1]))
pre=0
cnt=1
ans=[]
for p,y,i in py:
    if pre==p:
        cnt+=1
    else:
        cnt=1
        pre=p
    u=str(p).zfill(6)
    d=str(cnt).zfill(6)
    ans.append((u+d,i))
ans.sort(key=lambda x:x[1])
for k,v in ans:
    print(k)