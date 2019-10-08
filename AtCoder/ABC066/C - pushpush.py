# 2019/07/06

n=int(input())
a=list(input().split())

even,odd=[],[]

for i in range(n):
    if i%2==0:even+=[a[i]]
    else:odd+=[a[i]]

if n%2==0:print(*odd[::-1]+even)
else:print(*even[::-1]+odd)

# 解説を見て

from collections import deque

n=int(input())
a=list(input().split())

que=deque()

for i in range(n):
    if n%2==i%2:que.append(a[i])
    else:que.appendleft(a[i])
print(*que)

