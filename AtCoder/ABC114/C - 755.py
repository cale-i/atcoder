# 2019/08/27

n=int(input())
ln=len(str(n))
sft='7530'
cnt=0
def dfs(ln,s):
    global cnt
    if ln==0:
        if '7' in s and '5' in s and '3' in s:
            if '0' in str(int(s)):return
            if n>=int(s):cnt+=1
        return
    for e in sft:
        dfs(ln-1,s+e)
dfs(ln,'')

print(cnt)

# 写経

n=int(input())

def dfs(s):
    if int(s)>n:return 0
    
    ret=1 if all(s.count(c)>0 for c in '753') else 0
    for c in '753':
        ret+=dfs(s+c)
    return ret

print(dfs('0'))