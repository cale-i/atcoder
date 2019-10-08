# 2019/08/11

from collections import Counter

n=int(input())
a=list(map(int,input().split()))

c=Counter(a)

if c.most_common(1)[0][1]>2 or c[0]>1:
    print(0)
    exit()

for k,v in c.items():
    if k!=0 and v!=2:
        print(0)
        exit()
    if n%2==k%2:
        print(0)
        exit()
        
print(2**(n//2)%(10**9+7))