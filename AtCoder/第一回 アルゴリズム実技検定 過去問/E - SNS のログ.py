# 2020/01/15

n,q=map(int,input().split())
s=[tuple(map(int,input().split())) for _ in range(q)]

edge=[set() for _ in range(n)]

def follow(a,b):
    edge[a].add(b)


def re_follow(a):
    for i,e in enumerate(edge):
        if a in e:
            edge[a].add(i)

def f_follow(a):
    tmp=set()
    for e in edge[a]:
        tmp|=edge[e]
    edge[a]|=tmp

for qry in s:
    if len(qry)>2:
        qq,a,b=qry
        a-=1;b-=1
        follow(a,b)

    else:
        qq,a=qry
        a-=1
        if qq==2:
            re_follow(a)
        else:
            f_follow(a)

for idx,e in enumerate(edge):
    if idx in e:e.remove(idx)
    for i in range(n):
        if i in e:print('Y',end='')
        else:print('N',end='')
    print()