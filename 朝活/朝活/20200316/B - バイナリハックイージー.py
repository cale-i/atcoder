# https://atcoder.jp/contests/abc043/tasks/abc043_b

s=input()

res=[]
for e in s:
    if e=='B':
        if res:
            res.pop()
        else:continue
    else:
        res.append(e)
print(*res,sep='')