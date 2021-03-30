# 2019/12/22

n=int(input())
if n%2:print(0);exit()
n//=10
n=list(str(n))[::-1]
ans=int(n[0])
two=1 if int(n[0])>=2 else 0
five=1 if int(n[0])>=5 else 0
for i in range(1,len(n)):
    tmp=int(n[i])
    ans+=tmp*(10**i+2)
    if tmp>=2:two+=1
    if tmp>=5:five+=1
ans+=min(two,five)
print(ans)