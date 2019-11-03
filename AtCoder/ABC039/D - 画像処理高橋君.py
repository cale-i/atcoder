# 2019/11/2

import copy

h,w=map(int,input().split())
g=[list('#'*(w+2))]
for i in range(h):
    g+=[list('#'+input()+'#')]
g+=[list('#'*(w+2))]

res=[['.']*(w+2) for _ in range(h+2)]

dir=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for i in range(1,h+1):
    for j in range(1,w+1):
        if g[i][j]=='.':continue
        for dy,dx in dir:
            if g[i+dy][j+dx]=='.':break
        else:
            res[i][j]='#'
res2=copy.deepcopy(res)

for i in range(1,h+1):
    for j in range(1,w+1):
        if res[i][j]=='.':continue
        for dy,dx in dir:
            res2[i+dy][j+dx]='#'
        
for i in range(1,h+1):
    if res2[i][1:w+1]==g[i][1:w+1]:continue
    print('impossible')
    exit()
else:
    print('possible')
    for i in range(1,h+1):
        print(''.join(res[i][1:w+1]))