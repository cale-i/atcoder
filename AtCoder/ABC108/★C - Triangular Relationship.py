# 2019/09/10
# かんにんぐ

n,k=map(int,input().split())
cnt=0
a=n//k
b=(n+(k//2))//k if k%2==0 else 0
print(a**3+b**3)

# 2019/09/10
# かんにんぐ

n,k=map(int,input().split())
cnt=0
"""
余りの個数を配列に格納する
"""
num=[0]*(k+1)
for i in range(1,n+1):
    num[i%k]+=1

for a in range(k):
    b=(k-a)%k
    c=(k-a)%k
    if (b+c)%k:continue
    cnt+=num[a]*num[b]*num[c]
    
print(cnt)
