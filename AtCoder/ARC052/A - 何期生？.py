# 2019/11/1

import re

s=input()
ans=re.search(r'\d{1,2}',s)
print(ans.group())