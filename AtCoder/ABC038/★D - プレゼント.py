# 2019/07/04
# BIT らしい
# 全然わからん
# ↓WA

import sys

input=sys.stdin.readline

n=int(input())

wh=[]
for i in range(n):
    w,h=map(int,input().split())
    wh.append(tuple((w,h)))


wh.sort(key=lambda x:(-x[0],-x[1]))

cnt=0
pre_w,pre_h=float('inf'),float('inf')
for w,h in wh:
    if w<pre_w and h<pre_h:
        cnt+=1
        pre_w,pre_h=w,h
print(cnt)
