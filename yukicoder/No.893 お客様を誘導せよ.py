# 2020/01/19

from collections import deque

n=int(input())
pa=deque()

for _ in range(n):
    _,*a=map(int,input().split())
    if a:
        pa.append(a[::-1])

ans=[]
while pa:
    a=pa.popleft()
    ans.append(a.pop())
    if a:
        pa.append(a)
print(*ans)