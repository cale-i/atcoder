# 2019/08/03

from bisect import bisect_left

n=int(input())
a=[]
for i in range(n):
    c=int(input())
    a.append(c)

b=[i for i in range(1,2*n+1) if i not in a]    

a.sort()
b.sort()

turn=0 # 1==a,0==b
onfld=a[0]
del a[0]

def desc(x,onfld):
    idx=bisect_left(x,onfld)
    if idx==len(x):
        return None
    
    onfld=x[idx]
    del x[idx]
    return onfld


while a and b:
    if turn:    
        onfld=desc(a,onfld)
        while onfld is None and b:
            onfld=desc(b,0)
            if b:onfld=desc(a,onfld)
            
        turn=0
    else:
        onfld=desc(b,onfld)
        while onfld is None and a:
            onfld=desc(a,0)
            if a:onfld=desc(b,onfld)
        turn=1
        
print(len(b))
print(len(a))