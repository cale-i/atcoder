# 2019/08/20

# ↓いもす法って言うらしい
# BIT・セグメントツリーでも実装できるらしい
import sys
input=sys.stdin.readline

n,q=map(int,input().split())
res=[0]*(n+1)

for i in range(q):
    l,r=map(int,input().split())
    l-=1;r-=1
    res[l]+=1
    res[r+1]-=1

ans=''
cnt=0

for i in range(n):
    cnt+=res[i]    
    ans+=str(cnt%2)
print(ans)