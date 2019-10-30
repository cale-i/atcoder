# 2019/10/30

c=int(input())
n,m,l=[0]*c,[0]*c,[0]*c
for i in range(c):
    n[i],m[i],l[i]=sorted(map(int,input().split()))
print(max(n)*max(m)*max(l))