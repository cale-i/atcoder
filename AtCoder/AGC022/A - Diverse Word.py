# 2019/08/12

s=input()
if s=='zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()

st=set(s)

if len(s)<26:
    for i in range(97,97+26+1):
        if chr(i) in st:continue
        print(s+chr(i))
        exit()

s=list(s)
res=[s.pop()]

def solve(s):
    for _ in range(len(s)):
        tmp=s.pop()
        if tmp>res[-1]:
            res.append(tmp)
            res.sort()
        else:            
            for e in res:
                if e<tmp:continue
                s.append(e)
                return s

print(''.join(solve(s)))