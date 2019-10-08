# 2019/09/18
# 死ね

import sys
input=sys.stdin.readline

n=int(input())
cnt=0
pre=0
for i in range(n):
    a=int(input())
    if a==0:
        pre=0
        continue
    if pre:
        cnt+=1            
        a-=1
    buf=a//2
    a-=buf*2
    cnt+=buf
    pre=a

print(cnt)
