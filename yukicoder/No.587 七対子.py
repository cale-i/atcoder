# yukicoder No.587 七対子No.587 七対子 2020/01/27

from collections import Counter
C=Counter(input())

flag=False
ans='Impossible'
for k,v in C.items():
    if v==2:continue
    elif v==1:
        if flag:
            print(ans)
            exit()
        else:
            flag=True
            res=k
    else:
        print(ans)
        exit()
else:
    print(res)