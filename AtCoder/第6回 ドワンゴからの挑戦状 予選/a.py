# 2020/01/11

n=int(input())
s=[tuple(input().split()) for _ in range(n)]
w=input()

cnt=0
flag=False
for e in s:
    if flag:
        cnt+=int(e[1])
    if e[0]==w:
        flag=True
    
print(cnt)