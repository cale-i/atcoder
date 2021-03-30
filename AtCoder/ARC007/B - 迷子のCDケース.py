# 2019/11/25

n,m=map(int,input().split())
case=list(range(n+1))
for i in range(m):
    d=int(input())
    idx=case.index(d)
    case[idx],case[0]=case[0],case[idx]
print(*case[1:],sep='\n')