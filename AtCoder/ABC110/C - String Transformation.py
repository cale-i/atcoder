# 2019/08/16

s=list(input())
t=list(input())

c1={}
c2={}
for ss,tt in zip(s,t):
    if c1.get(ss) is None:
        c1[ss]=tt
    if c2.get(tt) is None:
        c2[tt]=ss
    if c1[ss]==tt and c2[tt]==ss:continue
    else:
        print('No')
        exit()

print('Yes')


# ↓いっぱいTLEしたやつ
# dictのvalueに対してset取ったりcount取ったりすると重い
# set(c1[ss])==tt and set(c2[tt])==ss の場合はなんか通った('ss','tt'がstrのためWAだった)
# set(c1[ss])==set(tt) and set(c2[tt])==set(ss)の場合はTLE
# 2019/08/16

s=list(input())
t=list(input())

c1={}
c2={}
for ss,tt in zip(s,t):
    c1[ss]=c1.get(ss,'')+tt
    c2[tt]=c2.get(tt,'')+ss
    
    if len(c1[ss])<2 and len(c2[tt])<2:continue
    if c1[ss].count(tt)==len(c1[ss]) and c2[tt].count(ss)==len(c2[tt]):continue #←この辺が重い原因だと思う
    else:
        print('No')
        exit()

print('Yes')
