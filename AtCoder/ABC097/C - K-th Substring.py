# 2019/08/06

s=input()
k=int(input())
ls=len(s)

ans=set(s)
for i in range(2,k+1):
    l=1
    res=s[0:i]
    while l<ls-i+1:
        ans.add(res)
        r=l+i-1
        res=res[1:]+s[r]
        l+=1
    ans.add(res)
ans=sorted(list(ans))
print(ans[k-1])