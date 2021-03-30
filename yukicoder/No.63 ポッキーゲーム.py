# 2019/12/28

l,k=map(int,input().split())
yu=l//(k*2)
print(yu*k if l%(k*2) else max(0,(yu-1)*k))