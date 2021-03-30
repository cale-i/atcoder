# 2019/12/08

n=int(input())
L=[]
for i in range(n):
    ls=[-1]*n
    a=int(input())
    for j in range(a):
        x,y=map(int,input().split())
        ls[x-1]=y
    L.append(ls)

ans=0
for bit in range(1,2**n):
    res=[-1]*n
    idx=0
    while idx<=len(bin(bit))-2:
        if bit&(1<<idx):    
            ret=[]
            for a,b in zip(res,L[idx]):
                ret.append(a&b)
        idx+=1
        
    if bin(bit)=='ob'+''.join(map(str,ret)).replace('-1','1'):
        ans=max(ans,ret.count('1'))
print(ans)