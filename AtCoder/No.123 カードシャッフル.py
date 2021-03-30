# yukicoder No.123 カードシャッフル 2020/02/12

# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# res=list(range(1,n+1))
# for i in range(m):
#     idx=a[i]-1
#     tmp=res[idx]
#     res.remove(tmp)
#     res=[tmp]+res
# print(res[0])


# 解答みて実装
n,m=map(int,input().split())
a=list(map(int,input().split()))
ans=1
for i in reversed(range(m)):
    if ans==1:
        ans=a[i]
        continue
    if a[i]==1:continue
    if a[i]>=ans:
        ans-=1
print(ans)