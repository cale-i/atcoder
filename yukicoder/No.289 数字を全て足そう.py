# 2019/12/28

s=input()
ans=0
for e in s:
    ans+=int(e) if e.isdecimal() else 0
print(ans)