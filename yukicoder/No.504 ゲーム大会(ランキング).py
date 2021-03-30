# yukicoder No.504 ゲーム大会(ランキング) 2020/01/28

n=int(input())
a=[int(input()) for _ in range(n)]

k=a[0]
rank=1
print(1)
for i in range(1,n):
    if a[i]>k:
        rank+=1
    print(rank)