import re

s=input()
ans=re.search(r'C.*F',s)
print('Yes' if ans else 'No')
