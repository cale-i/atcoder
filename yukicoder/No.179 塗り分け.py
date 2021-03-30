# 2020/01/01
# 解答かんにんぐ
# 遅い！(2500msくらい)

from copy import deepcopy

h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]


def check(x,y):
    g=deepcopy(s)
    flag=False
    for i in range(h):
        for j in range(w):
            if g[i][j] in ['.','R','B']:continue
            if i+y<0 or i+y>=h or j+x<0 or j+x>=w:return False
            if g[i][j]==g[i+y][j+x]=='#':
                flag=True
                g[i][j]='R'
                g[i+y][j+x]='B'
            else:return False
    return flag


for x in range(-w,w+1):
    for y in range(-h,h+1):
        if x==y==0:continue
        res=check(x,y)
        if res:
            print('YES')
            exit()
print('NO')


# ↓良さげな解答
# 早い！(250msくらい)

# from itertools import *
# from bisect import *
# # from math import *
# from collections import *
# from heapq import *
# from random import *
# from decimal import *
# import numpy as np
# import sys
# import copy

# sys.setrecursionlimit(10 ** 6)
# int1 = lambda x: int(x) - 1
# p2D = lambda x: print(*x, sep="\n")
# def II(): return int(sys.stdin.readline())
# def MI(): return map(int, sys.stdin.readline().split())
# def MI1(): return map(int1, sys.stdin.readline().split())
# def MF(): return map(float, sys.stdin.readline().split())
# def LI(): return list(map(int, sys.stdin.readline().split()))
# def LI1(): return list(map(int1, sys.stdin.readline().split()))
# def LF(): return list(map(float, sys.stdin.readline().split()))
# def LLI(rows_number): return [LI() for _ in range(rows_number)]
# dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# def main():
#     def check(di,dj):
#         for i in range(h):
#             for j in range(w):
# 6                if t[i][j] and first[i][j]:
#                     if not 0<=i+di<h:return False
#                     if not 0<=j+dj<w:return False
#                     if not t[i+di][j+dj]:return False
#                     first[i+di][j+dj]=False
#         return True

#     h, w = MI()
#     t = [[c == "#" for c in input()] for _ in range(h)]
#     si,sj=-1,-1
#     for i in range(h):
#         for j in range(w):
#             if t[i][j]:
#                 if si==-1:
#                     si,sj=i,j
#                 else:
#                     first=[[True]*w for _ in range(h)]
#                     if check(i-si,j-sj):
#                         print("YES")
#                         exit()
#     print("NO")
# main()
