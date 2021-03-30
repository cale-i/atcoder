# 2019/07/24
# 考え方 先頭を1 or 0 に固定し、最小を出力

s=list(input())

a=['1','0']
b=['0','1']

cnta=0
cntb=0

for i in range(len(s)):
    r=i%2
    if s[i]!=a[r]:cnta+=1
    elif s[i]!=b[r]:cntb+=1

print(min(cnta,cntb))