# 2019/09/17

n=int(input())
total=0
tax=1.05
for i in range(n):
    a,b=map(int,input().split())
    total+=a*b

print(int(total*tax))