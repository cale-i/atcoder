# 2019/07/23

input=open(0).readline

n,m=map(int,input().split())
py=[]
for i in range(m):
    p,y=map(int,input().split())
    py.append((p,y,i+1))

py.sort()

ans=[]

pre_cty=0
cnt=1
for i in range(m):
    p,y,idx=py[i]
    cty=p
    if pre_cty==cty:
        cnt+=1   

    else:
        pre_cty=p
        cnt=1
    
    p=str(p).zfill(6)
    x=str(cnt).zfill(6)
    ans.append((idx,p+x))

ans.sort()

for i in range(m):
    print(ans[i][1])