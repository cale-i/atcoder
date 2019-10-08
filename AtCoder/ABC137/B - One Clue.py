# 2019/08/10

k,x=map(int,input().split())
ans=[]
for i in range(k*2-1):
    ans.append(x-(k-1)+i)
print(*ans)