# 2019/09/16

n=int(input())
a=sorted(list(map(int,input().split())))
cnt=0

res=set()

for e in a:
    if e%2==0:
        while not e&1:
            e>>=1
    res.add(e)
print(len(res))




# ↓高速でうごくの見つけた
# ABC019C - 高橋くんと魔法の箱
n=int(input())
a=list(map(int,input().split()))
res=set()
for i in a:
    res.add(i//(i&-i)) # ここが高速化のポイント

print(len(res))
