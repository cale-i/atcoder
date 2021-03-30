def power(x,n,mod):
    #mod=10**9+7
    ret=1
    while n:
        if n&1:
            ret*=x
            ret%=mod

        x*=x
        x%=mod
        n>>=1
    return ret

"""
x=2
y=10**16
mod=10**9+7
print(power(x,y)%mod)
"""

