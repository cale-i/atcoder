# 2019/12/29
# ランレングス

n,k=map(int,input().split())
point=list(map(int,input().split()))
t=input()

rsp={'r':0,'s':1,'p':2}

ls=[[] for _ in range(k)]

for i in range(n):
    ls[i%k].append(t[i])    
ans=0
for e in ls:
    cnt=1
    for i in range(1,len(e)):
        if e[i-1]==e[i]:
            cnt+=1
        else:
            pp=(rsp[e[i-1]]-1+3)%3
            ans+=-(-cnt//2)*point[pp]
            cnt=1
    pp=(rsp[e[-1]]-1+3)%3
    ans+=-(-cnt//2)*point[pp]


print(ans)