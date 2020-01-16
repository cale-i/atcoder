# 2020/01/16

n=int(input())
A=[[0]*n for _ in range(n)]

for i in range(n-1):
    a=list(map(int,input().split()))
    for j,e in enumerate(a,i+1):
        A[i][j]=e
        

def calc(bit):
    if bit==0:return 0
    bit=bin(bit)[2:][::-1]
    
    psn=[]
    res=0
    for i in range(len(bit)):
        if bit[i]=='1':
            psn.append(i)

    for i in psn:
        for j in psn:
            if i==j:continue
            res+=A[i][j]            
    return res        

def solve(cmbs):
    res=0
    for bit in cmbs:
        if bit in scores:
            res+=scores[bit]
        else:
            ret=calc(bit)
            res+=ret
            scores[bit]=ret
    return res

ans=float('-inf')
scores={}

for bit_a in range(2**n):
    for bit_b in range(2**n):
        if bit_a & bit_b !=0:continue

        bit_c=(2**n-1)^(bit_a^bit_b)
            
        cmbs=tuple(sorted([bit_a,bit_b,bit_c]))
       
        
        res=solve(cmbs)
        ans=max(ans,res)
       

print(ans)