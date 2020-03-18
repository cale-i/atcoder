# https://atcoder.jp/contests/abc145/tasks/abc145_c

from itertools import permutations

n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
P=list(permutations(xy))
cnt=0

def dst(x1,x2,y1,y2):
    return pow(pow(x1-x2,2)+pow(y1-y2,2),0.5)


for p in P:
    for i in range(n-1):
        cnt+=dst(p[i][0],p[i+1][0],p[i][1],p[i+1][1])

print(cnt/len(P))