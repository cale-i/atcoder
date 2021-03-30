# 2019/10/24
# 解答かんにんぐ

s=input().replace('BC','X')
n=len(s)
cnt=0
ans=0
for i in range(1,n):
    tmp=s[i-1]+s[i]
    if s[i-1]=='A':
        cnt+=1
    if tmp[1]=='X':
        ans+=cnt
    if tmp not in ['AX','AA','XX','XA']:
        cnt=0
print(ans)