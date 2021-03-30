# 2020/01/15

s=input()
word=[]
flag = False
tmp=''

def is_upper(e):
    return 65<=ord(e)<=90

for e in s:
    tmp+=e
    if is_upper(e):
        if flag:
            flag = False
            word.append((tmp.lower(),tmp))
            tmp=''
        else:
            tmp=e
            flag = True
word.sort()

for e in word:
    print(e[1],end='')
print()