# yukicoder No.559 swapAB列 2020/01/27

s=input()
a=s.count('A')
cnt=0
for e in s:
    if e=='A':
        a-=1
        continue
    cnt+=a
print(cnt)