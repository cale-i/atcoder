# 2019/08/27

import sys
sys.setrecursionlimit(10**9)

h,w=map(int,input().split())
w+=2

g=[list('@'*w)]
for i in range(h):
    g+=[['@']+list(input())+['@']]

g+=[list('@'*w)]
print(*g)

cood=[]

def dfs(s):
    global cood


for i in range(1,h+1):
    for j in range(1,w):
        if g[i][j]=='.':continue
        