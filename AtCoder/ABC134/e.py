import sys
from collections import Counter

input=sys.stdin.readline

n=int(input())
a=[int(input()) for _ in range(n)]

c=Counter(a)

k,v=zip(*c.most_common())
print(max(2,v[0]))