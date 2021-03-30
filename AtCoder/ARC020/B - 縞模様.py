# 2019/11/12

n,c=map(int,input().split())
a=[int(input()) for _ in range(n)]    
even={}
odd={}
for i in range(n):
    if i%2:
        odd[a[i]]=odd.get(a[i],0)+1
    else:
        even[a[i]]=even.get(a[i],0)+1

en=-(-n//2)
on=n//2

ans=10**9
for ek,ev in even.items():
    for ok,ov in odd.items():
        if ek==ok:continue
        ans=min(ans,(en-ev)+(on-ov))
if ans==10**9:
    ans=on
print(ans*c)