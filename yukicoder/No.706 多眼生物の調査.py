# yukicoder No.706 多眼生物の調査 2020/01/24

from collections import Counter

n=int(input())
s=Counter([input().count('^') for _ in range(n)])
s=sorted(list(s.items()),key=lambda x: (x[1],x[0]),reverse=True)
print(s[0][0])