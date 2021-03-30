# 2019/08/27
# DFS
# 深さ優先探索
"""
n=int(input())
def dfs(n,s):
    if n==0:
        return print(s)
    for e in 'abc':
        dfs(n-1,s+e)
    return
s=''
dfs(n,s)"""

# 別解(遅い)

from itertools import combinations_with_replacement

n=int(input())
abc=list('abc'*n)
ans=list(set(combinations_with_replacement(abc,n)))
ans.sort()
for e in ans:
    print(''.join(e))
