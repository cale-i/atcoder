# 2019/12/10

s=list(input())[::-1]
n=len(s)
for i in range(n-1):
    if s[i]=='A' and s[i+1]=='W':
        s[i]='C'
        s[i+1]='A'
print(''.join(s[::-1]))
        
    