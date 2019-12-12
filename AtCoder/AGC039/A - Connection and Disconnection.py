# 2019/12/12

s=list(input())
k=int(input())
if k>1:s*=2
n=len(s)
f_cnt=0
s_cnt=0
for i in range(1,n):
    if s[i]==s[i-1]:
        s[i]='@'
        if i<=(n//2-1):f_cnt+=1
        else:s_cnt+=1
if k%2:
    cnt=(f_cnt)*-(-k//2)+s_cnt*(k//2)
else:
    cnt=(f_cnt+s_cnt)*(k//2)
if s[0]==s[-1]:
    cnt+=k-1
print(cnt)