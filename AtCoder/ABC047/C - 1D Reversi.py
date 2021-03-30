# 2019/08/08

s=input()
BW='B' if s[0]=='B' else 'W'
cnt=0

for i in range(len(s)):
    if s[i]==BW:continue
    BW=s[i]
    cnt+=1
print(cnt)