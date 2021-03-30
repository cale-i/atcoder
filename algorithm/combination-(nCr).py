# 組み合わせ計算(nCr)をそこそこ高速に計算するライブラリ
# 拡張ユークリッドの互除法による逆元計算を使用

# [使用可能条件]
# ・1<=r<=n<=10**6(c++なら10**7まで)
# ・pは素数 実装上ではp>nを仮定している

# nCr 
# = n! / r!(n−r)! 
# = (n!)×(r!)−1×((n−r)!)−1

# [時間計算量]
# 前処理 com_init():O(n)
# クエリ処理 com(n,r):O(1)
# http://drken1215.hatenablog.com/entry/2018/06/08/210000
"""
class Combination():
    def __init__(self,n,mod=10**9+7):
        self.fac=[1,1]
        self.finv=[1,1]
        self.inv=[0,1]

        for i in range(2,n+1):
            self.fac.append(self.fac[i-1]*i%mod)
            self.inv.append(mod-self.inv[mod%i]*(mod//i)%mod)
            self.finv.append(self.finv[i-1]*self.inv[i]%mod)        

    def comb(self,n,r,mod=10**9+7):
        if n<r:return 0
        if n<0|r<0:return 0
        return self.fac[n]*(self.finv[r]*self.finv[n-r]%mod)%mod
    
n=10
r=2

C=Combination(n)
print(C.com(n,r))
"""
# フェルマーの小定理ver
# なんか上のより早い

def cmb(n,r,mod=10**9+7):
    fac=[1,1]
    for i in range(2,n+1):
        fac.append(fac[i-1]*i%mod)
    ret=fac[n]*pow(fac[r]*fac[n-r]%mod,mod-2,mod)%mod
    return ret


n=10+7-2
r=6
print(cmb(n,r)) #10