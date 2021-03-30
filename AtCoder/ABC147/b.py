# 2019/12/08

s=list(input())
r=s[::-1]
n=len(s)
n=-(-n//2)
cnt=0
for i in range(n):
    if s[i]!=r[i]:cnt+=1
print(cnt)