# 2019/08/08

s=input()

cntB=0
ans=0
for i in range(len(s)):
    if s[i]=='B':cntB+=1
    else:ans+=cntB
print(ans)
