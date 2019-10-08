# 2019/07/12

n=int(input())
t=['TAKAHASHIKUN','Takahashikun','takahashikun']
w=list(input()[:-1].split())
cnt=0
for e in w:
    if e in t:
        cnt+=1
print(cnt)