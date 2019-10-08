# 場合の数復習!
# 考え方:部屋分け                                                      



# 青いボールをi分割する(k個のボールの間(k-1箇所)に仕切りを置く(i-1個))        => B  B  B  [k=3 i=2]
#                                                                            ↑  ↑   【k-1:仕切りを置く候補】【i-1:仕切りの数】

# 赤いボールを一列に並べる                                                 =>  R  R
# 赤いボールの左端・間・右端の中からi箇所選び､そこに青いボールのセットを置く   =>  R  R    [n=5]
#                                                                          ↑  ↑  ↑   [n-k+1:Rの間の数] [このうちi個を選ぶ] 
  
from math import factorial as fc

MOD=10**9+7
n,k=map(int,input().split())

for i in range(1,k+1):
    if n-k+1<i:   # <=ここで弾かないとRE
        print(0)
        continue
    b=fc(n-k+1)//fc(i)//fc(n-k+1-i)
    r=fc(k-1)//fc(i-1)//fc(k-1-(i-1))
    print(b%MOD*r%MOD)





# 2019/06/29 だめだったやつ
'''
import re
from itertools import permutations

n,k=map(int,input().split())
s=list('1'*k+'0'*(n-k))

pre=0
S=set(permutations(s))
for i in range(1,k+1):
    pat=r'1'*k
    reg=re.compile(pat)
    cnt=0
    for e in S:
        e=''.join(e)
        if reg.search(e):cnt+=1
    cnt-=pre
    print(cnt)
    pre+=cnt
    '''