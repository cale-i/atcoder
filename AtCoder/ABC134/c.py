import sys

input=sys.stdin.readline

n=int(input())
a=[-int(input()) for _ in range(n)]

A=sorted(a)


for i in range(n):
    if a[i]==A[-1] :
        print(A[-2])
    else:print(A[-1])
