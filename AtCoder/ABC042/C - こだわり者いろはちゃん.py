# 2019/08/17

n,k=map(int,input().split())
d=set(list(input().split()))

for i in range(n,10*n):
    if any([j in d for j in list(str(i))]):
        continue
    print(i)
    break