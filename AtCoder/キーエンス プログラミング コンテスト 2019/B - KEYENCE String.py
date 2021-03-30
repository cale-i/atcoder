# 2019/09/22

import re

s=input()
k='keyence'
n=len(s)

if re.search(r'^keyence',s) or re.search(r'keyence$',s):
    ans='YES'

rem=n-7
for i in range(n-rem+1):
    tmp=s[:i]+s[i+rem:]
    if tmp==k:
        ans='YES'
        break
else:ans='NO'
print(ans)