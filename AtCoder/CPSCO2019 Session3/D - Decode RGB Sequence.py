# 2019/07/27

n=int(input())
s=input()
if s[0]!='R' or s[-1]!='B':
    print('No')
    exit()
for i in range(1,n):
    if s[i-1]+s[i] not in ['RR','RG','GR','GB','BG','BB','BR']:
        print('No')
        exit()
    
print('Yes')

# シンプルに

n=int(input())
s=input()
if s[0]=='R' and s[-1]=='B':
    if 'RB' not in s and 'GG' not in s:
        print('Yes')
        exit()
print('No')