# 2019/10/03

import sys

inpt=sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
    a.append((int(input()),i+1))
a.sort()

cnt=0
for idx,aa in enumerate(a,1):
    if aa[1]%2==idx%2:continue
    cnt+=1
print(cnt//2)