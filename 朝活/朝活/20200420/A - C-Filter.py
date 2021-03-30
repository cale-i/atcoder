# https://atcoder.jp/contests/digitalarts2012/tasks/digitalarts_1

import re

s=list(input().split())
n=int(input())
t=[input().replace('*','.') for _ in range(n)]

for pat in t:
    regex=re.compile(r'^{}$'.format(pat))

    for i in range(len(s)):
        has_word=regex.search(s[i])
        if has_word:
            s[i]='*'*len(s[i])

print(*s)