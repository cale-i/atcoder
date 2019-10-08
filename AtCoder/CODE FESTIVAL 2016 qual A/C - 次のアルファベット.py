# 2019/09/17

s=list(input())
n=len(s)
k=int(input())

cnta=0
min_l=10000

for i in range(n):
    cnt=123-ord(s[i])
    if cnt>k:continue
    if s[i]=='a':
        cnta+=1
        continue
    s[i]='a'
    k-=cnt
    if k==0:break
else:
    last=s[-1]
    while cnta>=0:
        tmp=ord(last)-97
        kk=(k-cnta*26)%26
        
        min_l=min(min_l,(tmp+kk)%26)
        cnta-=1
    else:
        s[-1]=chr(min_l+97)
        
print(''.join(s))