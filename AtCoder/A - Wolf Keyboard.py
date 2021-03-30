# 2019/07/13

n,k=map(int,input().split())
a=[int(input()) for _ in range(n)]

a.sort(reverse=True)
cnt=sum(a[:k])+sum(a[k:]*2)
print(cnt)