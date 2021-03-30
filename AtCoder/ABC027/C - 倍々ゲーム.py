# 2019/08/27

n=int(input())

rank=0
while n:
    n//=2
    rank+=1
print(rank)

if rank%2:
    a=2
    b=a+1
else:
    b=2
    a=b+1

cnt=1
while cnt<n:
    cnt=a*cnt
    