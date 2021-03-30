# 2019/07/28

import re

pat1=re.compile(r'JOI')
pat2=re.compile(r'IOI')
pat3=re.compile(r'IOIOI')

s=input()

res1=re.findall(pat1,s)
res2=re.findall(pat2,s)
res3=re.findall(pat3,s)

print(len(res1))
print(len(res2)+len(res3))

# 普通の

s=input()

cnt1=0
cnt2=0
ln=len(s)
for i in range(ln-2):
    if s[i:i+3]=='JOI':cnt1+=1
    elif s[i:i+3]=='IOI':cnt2+=1

print(cnt1)
print(cnt2)