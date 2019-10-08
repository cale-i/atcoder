# 2019/07/04
# LIS

import bisect
import sys

input=sys.stdin.readline

n=int(input())
c=[int(input()) for _ in range(n)]

LIS=[float('inf')]

for i in range(n):
    if c[i]>LIS[-1]:
        LIS.append(c[i])
    else:
        idx=bisect.bisect_left(LIS,c[i])
        LIS[idx]=c[i]
print(n-len(LIS))