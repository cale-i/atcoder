# 2019/09/20

from collections import deque

s=input()
n=len(s)
def chk(s):
    s=''.join(s).replace('x','')
    if s!=s[::-1]:
        print(-1)
        exit()
chk(s)

s=deque(s)

res=[]
cnt=0
while len(s)>1:
    if s[0]==s[-1]:
        s.pop()
        res.append(s.popleft())
    else:
        if s[0]=='x':
            s.append('x')
        else:
            s.appendleft('x')
        cnt+=1
print(cnt)