# 2019/07/31

# 考え方
# 素因数分解した数 p を n個に分割 残りの数を適当な項に入れる
# eg.
# input
"""
4 972439611840
"""
# output
"""
206
"""
# 素因数分解=> 
# 2   :6
# 103 :4
# 3   :3
# 5   :1

# n個に分割
"""
//////////////////////
 1   2   3   4
----------------
 2   2   2   2
 *   *   *   *
103 103 103 103
 *
2^2
 *
103^0
 *
3^3
 *
5^1
----------------
111240  206  206  206
=972439611840
/////////////////////
"""


from fractions import gcd
from collections import Counter

n,p=map(int,input().split())

def trial_div(n):
    
    prime=Counter()

    for i in range(2,int(pow(n,0.5)+2)):
        while n%i==0:
            n//=i
            prime[i]+=1
    if n>1:prime[n]+=1
    
    return prime

res=trial_div(p)
ans=1
for k,v in res.items():
    tmp=k**(v//n)
    ans*=tmp

print(ans)