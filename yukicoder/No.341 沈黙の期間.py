# yukicoder No.341 沈黙の期間 2020/02/01

s=input()
cnt=0
ans=0
for e in s:
    if e=='…':
        cnt+=1
    else:
        ans=max(ans,cnt)
        cnt=0
else:
    ans=max(ans,cnt)
print(ans)