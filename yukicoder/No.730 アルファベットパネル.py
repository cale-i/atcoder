# yukicoder No.730 アルファベットパネル 2020/01/24

from collections import Counter

C=Counter(input())
print('YES' if C.most_common()[0][1]<2 else 'NO')