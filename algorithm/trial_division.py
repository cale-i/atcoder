# 試し割り法
# 因数分解に使用
# 計算量 O(√n*logn) (logn=>nが2のn乗の場合(最悪計算量)

from collections import Counter

def trial_div(n):
    
    prime=Counter()

    for i in range(2,int(pow(n,0.5)+2)):
        while n%i==0:
            n//=i
            prime[i]+=1
    if n>1:prime[n]+=1
    
    return prime

print(trial_div(int(input())))