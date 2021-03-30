# yukicoder No.349 干支の置き物 2020/02/01

from collections import Counter

n=int(input())
a=[input() for _ in range(n)]

c=Counter(a)
if c.most_common()[0][1]>-(-n//2):
    print('NO')
else:
    print('YES')