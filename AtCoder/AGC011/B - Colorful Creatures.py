# 2019/09/09

from itertools import accumulate

n=int(input())
a=sorted(list(map(int,input().split())))

acc=[0]+list(accumulate(a))
acc.pop()
acc.pop()
cnt=1
next=a.pop()

while a and acc:
    aa=a.pop()
    ac=acc.pop()
    if (aa+ac)*2>=next:
        cnt+=1
    else:break
    next=aa

print(cnt)