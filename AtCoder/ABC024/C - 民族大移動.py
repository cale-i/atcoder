# 2019/08/28
import sys
input=sys.stdin.readline

n,d,k=map(int,input().split())

lr=[tuple(map(int,input().split())) for _ in range(d)]


def solve(s,t):
    dir=1 if s<t else 0

    cp=s
    for idx,(l,r) in enumerate(lr,1):
        if l<=cp<=r:
            cp=r if dir else l
        if (dir and t<=cp) or (not dir and cp<=t):
            return idx


for i in range(k):
    s,t=map(int,input().split())
    print(solve(s,t))