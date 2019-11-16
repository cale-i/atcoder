# 2019/11/16

import sys
import itertools

sys.setrecursionlimit(10**7)
n=int(input())
xy=[]
for i in range(n):
    a,b=map(int,input().split())
    xy.append((a,b))

p=list(itertools.permutations(list(range(n)),n))

avg=0
for e in p:
    for i in range(n-1):
        avg+=pow((xy[e[i]][0]-xy[e[i+1]][0])**2+(xy[e[i]][1]-xy[e[i+1]][1])**2,0.5)
print(avg/len(p))