# 2019/12/29

# # O(n^2)->O(nlogn)
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# test=[]
# for i in range(n):
#     for j in range(n):
#         test.append(a[i]+a[j])
# res=sorted(test,reverse=True)
# print(res)
# print(sum(res[:m]))


n,m=map(int,input().split())
a=list(map(int,input().split()))
res=[a[-1]*2]
for i in range(n-1):
    res.append(a[i]*2)
    res.append(a[i]+a[i])
    res.append(a[i]+a[i])
ret=sorted(res,reverse=True)
print(ret)
print(sum(ret[:m]))
