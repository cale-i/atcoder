m=int(input())
N=[]
for _ in range(m):
    d,c=map(int,input().split())
    N+=[d]*c

def solve(N,cnt):
    n=len(N)
    ret=[]
    i=1
    while i<=n: 
        l=N[i-1]+N[i]
        if l<10:            
            ret.append(l)
            cnt+=1
            i+=1
        i+=1
    return ret,cnt

cnt=0
while len(N)>1:
    N,cnt=solve(N,cnt)
print(cnt)
        