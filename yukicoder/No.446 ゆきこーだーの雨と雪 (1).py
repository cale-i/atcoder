# yukicoder No.446 ゆきこーだーの雨と雪 (1) 2020/01/30

ab=[input() for _ in range(2)]

for e in ab:
    if not e.isdecimal():break
    if len(e)>1 and e[0]=='0':break
    if not (0<=int(e)<=12345):break
else:
    print('OK')
    exit()
print('NG')