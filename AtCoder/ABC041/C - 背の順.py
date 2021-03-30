# 2019/08/18

input()
a=list(map(int,input().split()))

ans=[]
for i,v in enumerate(a,1):
    ans.append((v,i))
ans.sort()

while ans:
    print(ans.pop()[1])    