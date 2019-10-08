# 2019/08/14

s=set(input())
if ('N' in s and 'S' not in s) or ('S' in s and 'N' not in s)\
   or ('W' in s and 'E' not in s) or ('E' in s and 'W' not in s):
   print('No')
else:
    print('Yes')


# きれいな書き方
s=set(input())
if ('N' in s)^('S' in s) or ('W' in s)^('E' in s):
    print('No')
else:
    print('Yes')  