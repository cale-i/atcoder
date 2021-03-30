# 2019/08/27

n=sorted(map(int,input().split()))

ans=set()
for i in n:
    for j in n:
        if i==j:continue
        for k in n:
            if i==k or j==k:continue
            ans.add(i+j+k)


ans=sorted(ans,reverse=True)
print(ans[2])
