# https://atcoder.jp/contests/digitalarts2012/tasks/digitalarts_1

import re

s=list(input().split())
n=int(input())
t=['^' + input().replace('*','.') + '$' for _ in range(n)]


for tt in t:
    regex=re.compile(tt)
    for i in range(len(s)):
        if regex.match(s[i]):
            s[i]='*'*len(s[i])
print(*s)