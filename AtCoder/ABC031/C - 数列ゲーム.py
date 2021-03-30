# 2019/09/04

n=int(input())
a=list(map(int,input().split()))
ans=float('-inf')
for i in range(n):
    ta=[]
    ao=[]

    for j in range(n):
        if i==j:continue
        if i>j:
            res=a[j:i+1]
        else:
            res=a[i:j+1]
        

        tmp=sum(res[::2])
        ta.append(tmp)
        ao.append(sum(res)-tmp)

    max_ao=max(ao)
    flag=True
    for idx,e in enumerate(ao):
        if e==max_ao and flag:
            ans=max(ans,ta[idx])
            flag=False
            break
        if not flag:break

print(ans)