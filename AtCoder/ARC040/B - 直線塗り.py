# 2019/11/14

n,r=map(int,input().split())
s=list(input())


for i,v in enumerate(s[::-1]):
    if v=='.':
        idx=n-(i+1)
        break
else:
    print(0)
    exit()
lst=max(idx-r+1,0)
ans=lst
i=0
painted=-1
while i<lst:
    if s[i]=='.' and painted<i:
        ans+=1
        painted=i+r-1
    i+=1
print(ans+1)