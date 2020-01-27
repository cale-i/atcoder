# yukicoder No.548 国士無双 2020/01/27

from collections import Counter

s=input()
kokushi=set('abcdefghijklm')
C=Counter(s)

flag=False

def _exit():
    print('Impossible')
    exit()

ans=set()
two=set()
for c in C.most_common():
    if c[1]>2:
        _exit()
    elif c[1]==2:
        if flag:_exit()
        else:
            flag=True
            two.add(c[0])
    else:
        ans.add(c[0])

if flag:
    ans=kokushi-(ans|two)

ans=sorted(ans)
print(*ans,sep='\n')