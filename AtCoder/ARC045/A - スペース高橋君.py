# 2019/10/01

s=list(input().split())

ans=[]
for e in s:
    if e[0]=='L':
        ans.append('<')
    elif e[0]=='R':
        ans.append('>')
    else:
        ans.append('A')
print(*ans)