# 2019/08/29

n,a,b,c,d=map(int,input().split())

s=input()
if c<d:
    flag=True
else:
    flag=False

if flag:
    for i in range(a,d-1):
        if s[i]==s[i+1]=='#':
            print('No')
            exit()
else:
    for i in range(b,d):
        if s[i-1]==s[i]==s[i+1]=='.':
            print('Yes')
            exit()

print('Yes' if flag else 'No')