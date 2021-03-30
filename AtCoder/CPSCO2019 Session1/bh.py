# 2019/12/14


def bh(s):

    from collections import Counter

    st=set(s)
    n=len(s)//len(st)
    c=Counter(s)

    for v in c.values():
        if v!=n:
            return 'No'
            
    else:
        return 'Yes'