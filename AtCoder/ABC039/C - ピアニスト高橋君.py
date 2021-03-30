# 2019/08/18

import re

s=input()

d=[('Do','WBWBWWBWBWBW'),
   ('Re','WBWWBWBWBW'),
   ('Mi','WWBWBWBW'),
   ('Fa','WBWBWBW'),
   ('So','WBWBW'),
   ('La','WBW'),
   ('Si','W')]

for k,v in d:
    if re.match(v,s):
        print(k)
        break