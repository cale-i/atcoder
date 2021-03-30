# 2019/07/11

n=int(input())
V=list(map(int,input().split()))
F=list(map(int,input().split()))

cnt=0
for v,f in zip(V,F):
    if v<f*2:cnt+=1
print(cnt)