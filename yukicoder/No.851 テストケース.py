# yukicoder No.851 テストケース 2020/01/20

n=int(input())
a=[]
for i in range(n):
    res=list(map(int,input().split()))
    if len(res)>1:
        print('"assert"')
        exit()
    a.append(*res)

ans=set()
for i in range(n):
    for j in range(n):
        if i==j:continue
        ans.add(a[i]+a[j])

ans=sorted(ans)[::-1]

print(ans[1%len(ans)])